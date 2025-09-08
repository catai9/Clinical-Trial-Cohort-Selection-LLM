from data_utils import regex_sentencize
from task import n2c22018Task, register_task
from few_shot_prompts import diet_supp_2mos_2018_examples

TASK_DIETSUPP_2MOS = 'DIETSUPP-2MOS'

@register_task(name='DIETSUPP-2MOS')
class DietSupp(n2c22018Task):
    """
    DIETSUPP-2MOS task
    
    Use of dietary supplements (excluding Vitamin D).
    
    "@register_task" calls register_task(name) and update the task registry.
    
    In the directory containing this class is listed in the parameters, this
    class will be imported and registered automatically. 
    This allows to add new tasks in this directory, without changing the code.
    
    Task classes with different names (register_task parameter) can solve the same task,
    but only one must be used at the same time
    """
    def __init__(self, config):
        super().__init__(config)
            
        # Task-specific parameters
        self.reset_every_sentence = self.config[TASK_DIETSUPP_2MOS]['reset_every_sentence']
        self.few_shot = self.config[TASK_DIETSUPP_2MOS]['few_shot']
    
        # Load diet supplement list
        dietsupp_list_file = self.config[TASK_DIETSUPP_2MOS]['resources']['DLSD_file']
        self.dietsupp_list = [e.strip() for e in open(dietsupp_list_file, 'r').readlines()]
            
    def get_task_name(self):
        """
        Returns
        -------
        task_name: str
            The official name of the classification task performed by this plugin.
        """
        return TASK_DIETSUPP_2MOS
        
    def get_task_classes(self):
        """
        Returns
        -------
        The default class corresponding to this classification task.
        """
        return ["not met", "met"]
        
    def get_default_class(self):
        """
        Returns
        -------
        The default class corresponding to this classification task.
        """
        return "not met"
        
    def filter_records_2months(self, text, text_id):
        """
        Split the text into different records 
        Keep only texts from less than two months
        """
        # 1. Get all records for this patient
        records = self.split_records(text)

        if any([date == 'unknown_date' for (date, _) in records]):
            if self.logger is not None:
                self.logger.debug('CHECK UNKNOWN DATE PROBLEM ({})!'.format(text_id))

        # Sort by date (not that 'unknown date' will go last if compare to numbers)
        records.sort(key=lambda s : str(s[0]))

        record_texts = [records[-1][1]]
        # 2. Get the date of the last record
        if records[-1][0] == 'unknown_date':
            pass
        else:
            last_date = records[-1][0]
            # 3. Get all texts < 2 months
            for i in range(-2, -(len(records)), -1):
                ## if the date is less than 2 months before the last date (last record)
                ## then keep the text
                ## otherwise, skip
                date = records[i][0]
                delta = last_date - date
                assert delta.days >= 0, '{} {} {}'.format(last_date, date, delta.days)
                if delta.days <= 61:
                    record_texts.append(records[i][1])
                else:
                    ...
                    #if not keep_2months_only:
                    #    texts.append(open(record_files[i], 'r').read())
        return record_texts

    def sentencize_with_section_titles(self, records):
        """
        Split the records into sections, and the sections into sentences
        Add the section title to each sentence, in order to "remember" in which section
        we are, when fed to the model

        Parameters
        ----------
        records: list of strings
            The records to split

        Returns
        -------
        sequences: list of strings
            The sequences after section splitting (records are merged together)

        titles: list of strings
            The titles 
        """

        sequences = []
        titles = []
        for record_text in records: 
            sections = self.split_sections(record_text)
            for section in sections:                
                title = section['title']
                text = section['text']
                sentences = [s for s, _, _ in regex_sentencize(text)]
                sequences.extend(sentences)
                titles.extend([title] * len(sentences))
        return sequences, titles        


    def get_best_passages(self, text_id, text, retriever, add_dietsupp_list=True):
        """
        Standard function to get the best passages for DIETSUPP task
        """
        ## Split the text into different records 
        record_texts = self.filter_records_2months(text, text_id)

        ## Split the remaining records into sections, and the sections into sentences
        ##   Add the section title to each sentence, in order to "remember" in which section
        ##   we are when fed to the model
        sequences, titles = self.sentencize_with_section_titles(record_texts)

        ################
        ## Go
        ################
        # Passage retrieval
        if add_dietsupp_list:
            task_query = ["dietary supplement"] + self.dietsupp_list
        else:
            task_query = ["dietary supplement"]
        sorted_kept_passages = retriever.get_best_passages((text_id, sequences),
                                                           (self.get_task_name(), task_query),
                                                           max_passages=5,
                                                           elbow_cutoff=True,
                                                           reset=True, logger=self.logger)
        sorted_kept_passages['titles'] = [titles[i] for i in sorted_kept_passages['indices']]
        return sorted_kept_passages
    
    
    
    def __call__(self, text_id, text, retriever, fastchat, preamble_type):
        """
        DIETSUPP-2MOS
        Use of dietary supplements (excluding Vitamin D)
        """
        
        # Passage retrieval
        sorted_kept_passages = self.get_best_passages(text_id, text, retriever, add_dietsupp_list=True)

        abstract = ""
        for i, passage in enumerate(sorted_kept_passages['passages']):
            abstract += '    ' + passage.strip() + "\n\n"

        if self.few_shot:        
            preamble = diet_supp_2mos_2018_examples.example_dictionary[preamble_type]
            fastchat.init_conversation(preamble)
            
            if self.logger is not None:
                self.logger.debug(f"The preamble conversation for {self.get_task_name()} is " + '\n'.join(preamble))
            
            prompt = '''
    Context: "{}"
            '''.format(abstract).strip()
            answer = ''
            
            if self.logger is not None:
                self.logger.debug('-------------------\nLINE: ' + abstract)
            fastchat.set_gen_param("temperature", 0) 
            result = fastchat.get_answer(prompt, logger=self.logger)
            answer = result['output']
            if self.logger is not None:
                self.logger.debug("ANSWER: " + answer)
            answer = answer.lower()
            if answer.endswith('yes.') or answer.endswith('yes'):
                return 'met'
            else:
                return 'not met'
        else:
            fastchat.reset_conversation()
            prompt = """
These are some sentences from a patient's clinical report. Answer Yes or No to the final question. 

{}

Question: Does the text mention that the patient uses a dietary supplement (excluding vitamin D)?
        """.format(abstract.rstrip()).strip()

            if self.logger is not None:
                self.logger.debug('-------------------\nPROMPT: ' + prompt)
            fastchat.set_gen_param("temperature", 0) 
            answer = fastchat.get_answer(prompt)['output']
            if self.logger is not None:
                self.logger.debug('\nANSWER: ' + answer)
            answer = answer.lower()
            if answer.startswith('yes'):
                answer = "met"
            else:
                answer = "not met"

            return answer