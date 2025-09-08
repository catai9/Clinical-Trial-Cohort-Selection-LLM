from data_utils import regex_sentencize
from task import n2c22018Task, register_task
from few_shot_prompts import all_smoker_classes_2006_examples

TASK_ALL_SMOKER_CLASSES = 'ALL-SMOKER-CLASSES'

@register_task(name='ALL-SMOKER-CLASSES')
class AllSmokerClasses(n2c22018Task):
    """
    ALL-SMOKER-CLASSES
    
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
        self.few_shot = self.config[TASK_ALL_SMOKER_CLASSES]['few_shot']
        
    def get_task_name(self):
        """
        Returns
        -------
        task_name: str
            The official name of the classification task performed by this plugin.
        """
        return TASK_ALL_SMOKER_CLASSES
        
    def get_default_class(self):
        """
        Returns
        -------
        The default class corresponding to this classification task.
        """
        return 4

    def get_task_classes(self):
        """
        Returns
        -------
        The default class corresponding to this classification task.
        """
        return [0, 1, 2, 3, 4]
            
    def __call__(self, text_id, text, retriever, fastchat, preamble_type):
        """
        ALL-SMOKER-CLASSES
        """
    
        # Passage retrieval
        task_query = ["smoking"]
        
        sentences = [s for s, _, _ in regex_sentencize(text)]

        sorted_kept_passages = retriever.get_best_passages((text_id, sentences),
                                                           (TASK_ALL_SMOKER_CLASSES, task_query),
                                                           max_passages=5,
                                                           elbow_cutoff=True,
                                                           reset=True, logger=self.logger)

        abstract = ""
        for i, passage in enumerate(sorted_kept_passages['passages']):
            abstract += '    ' + passage.strip() + "\n\n"

        if self.few_shot:        
            preamble = all_smoker_classes_2006_examples.example_dictionary[preamble_type]
            fastchat.init_conversation(preamble)
            
            if self.logger is not None:
                self.logger.debug(f"The preamble conversation for {TASK_ALL_SMOKER_CLASSES} is " + '\n'.join(preamble))
            
            prompt = '''
    Context: "{}"
            '''.format(abstract).strip()
            
            answer = ''
            # Start at temperature 0 to allow reproductibility
            fastchat.set_gen_param("temperature", 0) 
            result = fastchat.get_answer(prompt, logger=self.logger)
            answer = result['output']

            if self.logger is not None:
                #gen_prompt = result['prompt']
                self.logger.debug('-------------------\nLINE: ' + abstract)
            
            if self.logger is not None:
                self.logger.debug("ANSWER: " + answer)
            
            answer = answer.lower()
            if answer.endswith('current smoker.') or answer.endswith('current smoker'):
                return 0
            elif answer.endswith('past smoker.') or answer.endswith('past smoker'):
                return 1
            elif answer.endswith('non-smoker.') or answer.endswith('non-smoker'):
                return 2
            elif answer.endswith('smoker.') or answer.endswith('smoker'):
                return 3
            else:
                return 4
        else:
            fastchat.reset_conversation()
            prompt = """
These are some sentences from a patient's clinical report. Classify the patient as Current Smoker, Non-Smoker, Past Smoker, Smoker (unsure if current or past smoker), or Unknown. 

{}
        """.format(abstract.rstrip()).strip()

            if self.logger is not None:
                self.logger.debug('-------------------\nPROMPT: ' + prompt)
            # Start at temperature 0 to allow reproductibility
            fastchat.set_gen_param("temperature", 0) 
            # Get answer to 1st question
            answer = fastchat.get_answer(prompt)['output']
            if self.logger is not None:
                self.logger.debug('\nANSWER: ' + answer)
            answer = answer.lower()
            if 'current' in answer:
                return 0
            elif 'past' in answer:
                return 1
            elif 'non' in answer:
                return 2
            elif 'unknown' in answer:
                return 4
            elif 'smoker' in answer:
                return 3
            else:
                return 4
        