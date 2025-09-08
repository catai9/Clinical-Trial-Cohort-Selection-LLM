from sentence_transformers import SentenceTransformer, util
import spacy
import numpy as np
import torch
import sklearn
from scipy.spatial.distance import cosine
from sklearn.metrics import euclidean_distances
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
from torchmetrics.functional import pairwise_cosine_similarity

import ot

import fasttext
import fasttext.util

from tqdm import tqdm
from timeit import default_timer as timer
from data_utils import regex_sentencize

class DPR:
    def __init__(self):
        self.passage_encoder = SentenceTransformer('facebook-dpr-ctx_encoder-single-nq-base')
        self.query_encoder = SentenceTransformer('facebook-dpr-question_encoder-single-nq-base')
        
        self.query_embedding = None
        
    def set_query(self, query):
        self.query_embedding = self.query_encoder.encode(query)
        
    def dpr_similarity(self, text, query=None):
        if query is not None:
            self.set_query(query)
        if self.query_embedding is None:
            raise ValueError('You must set a query with set_query or with the query parameter')
        
        # Process the text using spaCy for sentence segmentation only
        doc = self.nlp(text)

        # Access sentences
        sentences = [s for s, _, _ in regex_sentencize(text)]

        passage_embeddings = self.passage_encoder.encode(sentences)    

        #Important: You must use dot-product, not cosine_similarity
        scores = util.dot_score(self.query_embedding, passage_embeddings)[0]
        #orted_indices = torch.argsort(scores, descending=True)
        #sorted_sentences = sentences[sorted_indices]
        return {
            'passages':sentences,
            'scores':scores
        }
    
    
class EmbeddingSimilarity:
    def __init__(self, config):
        self.config = config
        self.method = config['retrieval']['method'].upper()
        nlp = config['nlp']
        assert self.method in {"OVERLAP", "EMD"}
        
        if nlp is None:
            # Load only the sentence segmentation component
            self.nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
        else:
            self.nlp = nlp
        self.distance_type = config['retrieval'][self.method]['distance_type']
        self.embedding_type = config['retrieval'][self.method]['embedding_type']
        self.use_cuda = config['retrieval']['use_cuda']
        if self.embedding_type == "fasttext":
            fasttext_lang = 'en'
            fasttext_model = 'cc.en.300.bin'
            # fasttext.util.download_model(fasttext_lang, if_exists='ignore')
            self.fasttext_model = fasttext.load_model(fasttext_model)
            
        self.precomputed_indices = {}

    def index_query(self, queryid, texts, reset=False, verbose=False):
        if type(texts) == str:
            texts = [texts]
        results = [            
            self.index_doc(f'{queryid}_{i}', [texts[i]], reset=reset, verbose=verbose)
            for i in range(len(texts))
        ]
        return results
                  

    def index_doc(self, docid, document, reset=False, verbose=False):     
        """
        Parameters
        ----------
        docid : str 
            the id of the document
        text : iterator
            The list (or generator) of sequences already splitted.
        reset : bool, default False
            If True, overwrite the existing index if the docid already exists in the index.
            If False, do not overwrite.
        verbose: bool, default False

        Returns
        -------
        result : dict
            a dictionary representing the index
        """
        if docid in self.precomputed_indices and not reset:
            return self.precomputed_indices[docid]        
        else:
            if type(document) == str:
                raise TypeError('This is the old way of using this function, you must pass an already sentencized sequence')
                #sequences = [s for s, _, _ in regex_sentencize(doc)]            
            
            vectorizer = DictVectorizer(sparse=True)
            corpus_dict = []
            for sequence in document:
                # Process the text using spaCy for sequence segmentation only
                doc = self.nlp(sequence)
                sent_dict = {}
                for token in doc:
                    str_token = token.text.strip()
                    if self.config['retrieval']['lowercase']:
                        str_token = str_token.lower()
                    if len(str_token):
                        n = sent_dict.get(str_token, 0)
                        sent_dict[str_token] = n+1
                corpus_dict.append(sent_dict)

            count_matrix = vectorizer.fit_transform(corpus_dict)

            #  Embedding matrix
            #    Indices within this matrix are aligned with vocabulary indices
            embedding_matrix = [
                self.fasttext_model.get_word_vector(term)
                for term in vectorizer.get_feature_names_out()
            ]
            if self.use_cuda:
                embedding_matrix = torch.tensor(embedding_matrix).cuda()
            else:
                # We use numpy when working on CPU because pot.emd2 is way ~3x faster
                # with numpy than with torch
                embedding_matrix = np.array(embedding_matrix)

            assert len(document) == count_matrix.shape[0]
            results = {'passages': np.array(document)}
            results['count_matrix'] = count_matrix
            results['embedding_matrix'] = embedding_matrix
            results['vectorizer'] = vectorizer

            self.precomputed_indices[docid] = results
            return results

        
    def get_similarity(self, docid, doc, queryid, query, reset=False, return_details=False, logger=None):
        if logger is not None:
            logger.debug('Index document')
        doc_index = self.index_doc(docid, doc, reset=reset)
        if logger is not None:
            logger.debug('Index query')
        query_indices = self.index_query(queryid, query, reset=reset)
        assert type(query_indices) == list
        
        doc_embeddings = doc_index['embedding_matrix']
        
        if logger is not None:
            logger.debug('Build similarity matrix')
                                    
        # Compute EMD/Wasserstein distance between the vectors, based on 
        # the computed distance matrix.
        # Not clear whether CUDA can really make it faster, as the matrices
        # are pretty small at this point.
        # Efforts to use an approximation of Wasserstein distance (geomloss, sinkhorn)
        # have been unsuccessful but quickly abandoned, I must admit
        # (errors from the loss function).        
        doc_passages = doc_index['passages']
        doc_count_matrix = doc_index['count_matrix']
        doc_embedding_matrix = doc_index['embedding_matrix']
        
        doc_similarities = []
        for i in range(len(doc_passages)):
            passage_count_matrix = doc_count_matrix[i]
            
            #print('passage', doc_passages[i])
            
            # Get indices of terms that appear in the passage
            all_term_indices = passage_count_matrix.indices.tolist()
            # Build a one-hot dense vector with only those terms, for each passage
            # See documentation of csr_matrix, but basically the idea is NOT to convert the sparse vector
            # into a dense vector by the to_array() method, which produces a vector of the size of the entire vocabulary
            # and takes time to process. We then collect the indices and data from the csr_matrix object
            # and build the dense vectors manually from these information.
            passage_sparse_vector_data_dict = {i:v for i, v in zip (passage_count_matrix.indices, passage_count_matrix.data)}
            passage_dense_vector = np.array([passage_sparse_vector_data_dict.get(i, 0) for i in all_term_indices])
            # dense_vector: 1-D vector with the occurrence number of each terms, reduced to only 
            #   the terms appearing in the passage
            # Normalize
            passage_dense_vector /= passage_dense_vector.sum()
            # Passage embeddings
            passage_embeddings = doc_embeddings[all_term_indices]

            # keep the best similarity between a query and the passage
            passage_similarities = []
            for query_index in query_indices:
                query_embeddings = query_index['embedding_matrix']
                query_count_matrix = query_index['count_matrix']
                query_embedding_matrix = query_index['embedding_matrix']
                query_sparse_vector_data_dict = {i:v for i, v in zip (query_count_matrix.indices, query_count_matrix.data)}
                query_dense_vector = np.array([query_sparse_vector_data_dict.get(i, 0) for i in query_count_matrix.indices.tolist()])            
                # dense_vector: 1-D vector with the occurrence number of each terms, reduced to only 
                #   the terms appearing in the passage
                # Normalize
                query_dense_vector /= query_dense_vector.sum()

                # Build similarity matrix from vocabulary embeddings
                if self.distance_type == 'cosine':
                    if self.use_cuda:
                        # Torch cosine similarity return 0 on the diagonal (??)
                        # then 1 - cos_sim returns 1 on the diagonal
                        raise ValueError('untested')
                        local_dist_matrix = (1 - pairwise_cosine_similarity(query_embeddings, passage_embeddings))
                    else:
                        # Without CUDA we stay with numpy
                        # We use numpy when working on CPU because pot.emd2 is ~3x faster
                        # with numpy than with torch                
                        local_dist_matrix = sklearn.metrics.pairwise.cosine_distances(query_embeddings, passage_embeddings) # cosine_distance : ie 1-cos similarity = 1-cos(theta)
                elif distance_type == 'euclid':
                    if self.use_cuda:
                        raise NotImplementedError()
                    else:
                        raise ValueError('untested')
                        local_dist_matrix = euclidean_distances(query_embeddings, passage_embeddings)

                # Wasserstein/EMD distance 
                if self.method == "EMD":
                    emd_distance = ot.emd2(query_dense_vector, passage_dense_vector, local_dist_matrix)
                    similarity = -similarity
                elif self.method == "OVERLAP":
                    min_distances = local_dist_matrix.min(axis=1)
                    total_distance = np.sum(min_distances)
                    similarity = -total_distance
                    
                #print(similarity, query_index['passages'])
                passage_similarities.append(similarity)
            doc_similarities.append(max(passage_similarities))
            
        results = {
            'passages': doc_passages,
            'scores': np.array(doc_similarities)
        }
        
        if return_details:
            results.update({
                'doc_index': doc_index,
                'query_index': query_index,
            })
        return results
        


        
class Retriever:
    def __init__(self, config):
        self.method = config['retrieval']['method']
        self.config = config
        if self.method == 'DPR':
            self.retriever = DPR(config['nlp'])
        elif self.method in ('EMD', 'OVERLAP'):
            self.retriever = EmbeddingSimilarity(self.config)
        #elif mode == 'OVERLAP':
        #    self.retriever = Overlap(config['nlp'], 
        #                             distance_type=config['distance_type'], 
        #                             embedding_type=config['embedding_type'], 
        #                             use_cuda=config['use_cuda'])

    def get_similarity(self, 
                       text_info,
                       query_info,
                       reset=False, logger=None):
        (textid, text) = text_info
        (queryid, query) = query_info
        if self.method == 'DPR':
            results = self.retriever.dpr_similarity(text, query)
        elif self.method in ('EMD', 'OVERLAP'):
            results = self.retriever.get_similarity(textid, text, queryid, query, reset=reset, logger=logger)
#        elif self.mode == 'EMD':
#        elif self.mode == 'OVERLAP':
#            results = self.retriever.get_overlap_similarity(textid, text, queryid, query, reset=reset, logger=logger)
        return results

    def get_best_passages(self,
                          text_info,
                          query_info,
                          max_passages=5, elbow_cutoff=True,
                          reset=True, logger=None):
        (textid, text_sequences) = text_info
        (queryid, query) = query_info
        
        # remove duplicate sequences
        seen = set()
        text_sequences = [x for x in text_sequences if x not in seen and not seen.add(x)]
        
        passages = self.get_similarity((textid, text_sequences),
                                        (queryid, query),
                                        reset=True, logger=logger)
        
        sorted_indices = np.argsort(-passages['scores'])
        sorted_scores = passages['scores'][sorted_indices]

        if elbow_cutoff:
            # we will cut off at the largest gap between two consecutive scores
            # but we do not consider zeros or close zeros (which come from an exact match with the query,
            # and exact match are way more similar than any other match)
            gaps = [abs(sorted_scores[i+1] - sorted_scores[i]) if sorted_scores[i] < -0.0001 else 0 for i in range(len(sorted_scores)-1)]
            #print('sorted_indices', sorted_indices)
            #print('sorted scores ', sorted_scores)
            max_idx = np.argmax(gaps)
            #print('max idx', max_idx)
            kept_indices = sorted_indices[:min(max_passages, max_idx+1)]
            #print('kept_indices', kept_indices)
        else:
            kept_indices = sorted_indices[:max_passages]
        #for s, p in zip (sorted_scores, passages['passages'][sorted_indices]):
        #    print(s, p)
        
        sorted_kept_passages = passages['passages'][kept_indices]

        return {
            "passages": sorted_kept_passages, 
            "indices": kept_indices
        }
        
