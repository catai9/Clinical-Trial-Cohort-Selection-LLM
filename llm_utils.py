#!/usr/bin/env python

# SETUP: Add Imports
import torch
import pandas as pd
import numpy as np
import time
import logging
import spacy
import yaml
import argparse

from os import listdir, remove
from os.path import join, isfile, isdir, exists
from tqdm import tqdm
from lxml import etree
from yaml import CLoader as Loader

from retrieval_utils import Retriever
from answering_utils import FastChatInterface
from eval_utils import evaluation_expanded
from task import n2c22018Task, import_modules, TASK_REGISTRY

class LLMModel:
    def __init__(self, config_file, title_prefix, task_names, is_multiclass=False):
        self.test_samples = {}
        self.logger = None
        self.task_plugins = []
        self.debug = True
        self.retriever = None
        self.fastchat = None
        
        self.config_file = config_file # e.g., './model-configs/gptj6b_n2c2_2018.yml'
        self.title_prefix = title_prefix # e.g., 'b-few-shot-gpt-j-6b'
        self.task_names = task_names # ['ADVANCED-CAD' 'ALCOHOL-ABUSE' 'ASP-FOR-MI' 'CREATININE' 'DIETSUPP-2MOS' 'DRUG-ABUSE' 'ENGLISH' 'HBA1C' 'MAJOR-DIABETES' 'MAKES-DECISIONS' 'MI-6MOS' 'ABDOMINAL']
        self.is_multiclass = is_multiclass

        self.config = yaml.load(open(self.config_file, "r").read(), Loader=Loader)
        
    def setupLoggerHelperFunction(self):
        # Set up logger
        timestr = time.strftime("%Y%m%dT%H%M%S")
        logfile = f"log/{self.title_prefix}-log-{timestr}.txt"
        if exists(logfile):
            remove(logfile)

        self.logger = logging.getLogger("n2c2")
        while len(self.logger.handlers):
            self.logger.removeHandler(self.logger.handlers[0])
        self.logger.propagate = False

        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(logfile)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)

        self.logger.addHandler(stream_handler)
        self.config['logger'] = self.logger

        if self.logger is not None:
            self.logger.info("Parameters: \n" + yaml.dump(self.config, default_flow_style=True))
            if torch.cuda.is_available():
                self.logger.info(f'available devices: {torch.cuda.device_count()}')
                self.logger.info(f'current device: { torch.cuda.current_device()}')
            else:
                self.logger.info('No CUDA device available')
        
    def importTasksHelperFunction(self):
        # All modules from the task directories (as specified in the configuration file) are automatically imported. 
        # Within these automatic imports, all classes that inherit Task and are decorated by @register_task will be automatically registered in TASK_REGISTRY
        # This way, when we implement a new task, all we have to do is adding the new class in the task directories, no further modification on the main code is required
        for dir_name in self.config['main']['task_dirs']:
            import_modules(dir_name)

        # Check that the called task names are registered
        assert all([task_name in TASK_REGISTRY for task_name in self.task_names])

        # Create (construct) task objects (plugins)
        # TASK_REGISTRY[task_name] is a python class so TASK_REGISTRY[task_name](config) is a call to the class constructor with config as the only parameter
        # The result is then a list of Task objects, that will be called later
        self.task_plugins = [TASK_REGISTRY[task_name](self.config) for task_name in self.task_names]

        # Check that the tasks handled by the plugins are all different
        assert len(self.task_plugins) == len({t.get_task_name() for t in self.task_plugins}), "Some of your loaded plugins are made for the same task (from task.get_task_name())"
        
    def load2006and2008DataHelperFunction(self, data_split):
        data_dir = self.config['general'][data_split]['dir']
        assert isdir(data_dir)
        filename = self.config['general'][data_split]['files'][0]
        assert isfile(join(data_dir, filename))

        if self.logger is not None:
            self.logger.info('Load data')

        if filename.endswith('.csv'):
            filepath = join(data_dir, filename)
            return pd.read_csv(filepath)

        return pd.DataFrame()
    
    def load2018DataHelperFunction(self, data_split):
        data_dir = self.config['general'][data_split]['dir']
        assert isdir(data_dir)
        if 'files' in self.config['general'][data_split] and self.config['general'][data_split]['files'] is not None:
            filenames = self.config['general'][data_split]['files']
            assert all([isfile(join(data_dir, filename)) and filename.endswith('.xml') for filename in filenames])
        else:
            filenames = [filename for filename in listdir(data_dir) if filename.endswith('.xml')]

        if self.logger is not None:
            self.logger.info('Load data')
        variables = {'id': [], 'text': []}
        for filename in filenames:
            if filename.endswith('.xml'):
                filepath = join(data_dir, filename)
                tree = etree.parse(filepath)
                text = tree.xpath("TEXT")[0].text
                for tag in tree.xpath("TAGS")[0].getchildren():
                    if tag.tag not in variables:
                        variables[tag.tag] = [tag.get('met')]
                    else:
                        variables[tag.tag].append(tag.get('met'))
                variables['id'].append(filename)
                variables['text'].append(text)
                assert max([len(l) for _, l in variables.items()]) == min([len(l) for _, l in variables.items()])
        df_data = pd.DataFrame(variables)

        return df_data

    def loadModelParamsHelperFunction(self):
        # Parameters for answer identification
        model_path = self.config['generation']['model_path']
        device_params = self.config['device']

        # Params
        gen_params = self.config['generation']

        if self.logger is not None:
            self.logger.info('Load fastchat model ' + model_path)

        self.fastchat = FastChatInterface(
            model_path, device_params, gen_params, debug=self.debug
        )

        # Parameters for passage retrieval 
        method = self.config['retrieval']['method']  #'EMD', 'DPR', "OVERLAP"

        if method in {'EMD', 'OVERLAP'}:
            if self.logger is not None:
                logging.info('Load spaCy')
            nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
            self.config['nlp'] = nlp


        if self.logger is not None:
            self.logger.info('Load retriever')

        self.retriever = Retriever(self.config)

    def runPredictionHelperFunction(self, data, test_samples, data_split, preamble_type):
        self.logger.debug(f"Preamble Type: {preamble_type}")
        
        prediction_df = pd.DataFrame(data['id'])
        for task_name in self.task_names:
            prediction_df[task_name] = np.nan
        assert all([c in data.columns for c in prediction_df.columns])
        
        if self.is_multiclass:
            model_results = ({
                'Task':[],
                'Run': [],
                'Macro F1': [],
                'Micro F1': [],
                'None F1': []
            })
        else:
            model_results = ({
                'Task':[],
                'Run': [],
                'F1' :[]
            })
            
        df_model_results = pd.DataFrame(model_results)
        self.logger.debug(f'Create DataFrame: {df_model_results}\n')

        start = time.time()

        for task_plugin in self.task_plugins:
            task_name = task_plugin.get_task_name()
            self.logger.debug(f'Running task_name {task_name}')

            for i, raw in tqdm(data.iterrows(), total=data.shape[0]):
                text_id = raw['id']
                if len(test_samples) > 0 and text_id not in test_samples:
                    continue
                text = raw['text']

                if self.debug:
                    self.logger.debug(" <<<< " + str(text_id) + " >>>>")
                pred_answer = task_plugin(text_id, text, self.retriever, self.fastchat, preamble_type)

                prediction_df.loc[prediction_df['id'] == text_id, task_name] = pred_answer

                if self.debug:
                    expected_answer = raw[task_name]
                    self.logger.debug(f'PREDICTED {task_name}: {pred_answer}')
                    self.logger.debug(f'EXPECTED {task_name}: {expected_answer}')

                if self.debug:
                    scores = evaluation_expanded(data, prediction_df, [task_plugin], self.is_multiclass)

                    if self.is_multiclass:
                        macro_f1_score = scores[task_name].get('macro_f1_score')
                        micro_f1_score = scores[task_name].get('micro_f1_score')
                        none_f1_score = scores[task_name].get('none_f1_score')
                        self.logger.debug(f'---------{task_name}, {preamble_type}----------- macro_f1_score={macro_f1_score}; micro_f1_score={micro_f1_score}; none_f1_score={none_f1_score} -------------------------')

                    else: 
                        acc_str = scores[task_name].get('acc_str')
                        prec_str = scores[task_name].get('prec_str')
                        rec_str = scores[task_name].get('rec_str')
                        f1_score = scores[task_name].get('f1_score')
                        self.logger.debug(f'---------{task_name}, {preamble_type}----------- Acc={acc_str}; Prec={prec_str}; Recall={rec_str}; F1={f1_score} -------------------------')
                        fp = scores[task_name].get('fp')
                        tp = scores[task_name].get('tp')
                        fn = scores[task_name].get('fn')
                        tn = scores[task_name].get('tn')
                        self.logger.debug(f'---------{task_name}, {preamble_type}----------- FP={fp}; TP={tp}; FN={fn}; TN={tn} -------------------------')

            if self.is_multiclass:
                print(f'---------{task_name}, {preamble_type}----------- macro_f1_score={macro_f1_score}; micro_f1_score={micro_f1_score}; none_f1_score={none_f1_score} -------------------------')
                new_row = pd.DataFrame({'Task': task_name, 'Run': preamble_type, 'Macro F1': macro_f1_score, 'Micro F1': micro_f1_score, 'None F1': ', '.join(map(str, none_f1_score))}, index=[0])
            else:
                print(f'---------{task_name}, {preamble_type}----------- f1_score={f1_score} -------------------------')
                new_row = pd.DataFrame({'Task': task_name, 'Run': preamble_type, 'F1': f1_score}, index=[0])
            
            df_model_results = pd.concat([new_row, df_model_results.loc[:]]).reset_index(drop=True)
            
            end = time.time()

            print(f'Elapsed Time for: {end - start}')
            self.logger.debug(f'Elapsed Time for task {task_name}: {end - start}')

        timestr = time.strftime("%Y%m%dT%H%M%S")
        df_model_results.to_csv(f'results/{self.title_prefix}-{data_split}-{timestr}.csv')
        
        return scores

    def setupModelForPredictions(self):
        self.setupLoggerHelperFunction()
        self.importTasksHelperFunction()
        self.loadModelParamsHelperFunction()
        
    def run2018ModelPredictions(self, preamble_type):
        df_train_data = self.load2018DataHelperFunction("train")
        df_val_data = self.load2018DataHelperFunction("val")
        df_test_data = self.load2018DataHelperFunction("test")
        
        self.runModelPrediction(df_train_data, df_val_data, df_test_data, preamble_type)
        
    def load2006and2008ModelPredictions(self, preamble_type):
        df_train_data = self.load2006and2008DataHelperFunction("train")
        df_val_data = self.load2006and2008DataHelperFunction("val")
        df_test_data = self.load2006and2008DataHelperFunction("test")
        
        self.runModelPrediction(df_train_data, df_val_data, df_test_data, preamble_type)

    def runModelPrediction(self, df_train_data, df_val_data, df_test_data, preamble_type):
        train_scores = self.runPredictionHelperFunction(df_train_data, self.test_samples, "train", preamble_type)
        self.logger.debug(f'Train Scores = {train_scores}')

        val_scores = self.runPredictionHelperFunction(df_val_data, self.test_samples, "val", preamble_type)
        self.logger.debug(f'Val Scores = {val_scores}')
        
        test_scores = self.runPredictionHelperFunction(df_test_data, self.test_samples, "test", preamble_type)
        self.logger.debug(f'Test Scores = {test_scores}')
