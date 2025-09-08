from data_utils import regex_sentencize
from task import n2c22018Task, register_task
from few_shot_prompts import asp_for_mi_2018_examples

TASK_ASP_FOR_MI = 'ASP-FOR-MI'   # official task: use of aspirin to prevent myocardial infarction


@register_task(name='ASP-FOR-MI')
class AspForMI(n2c22018Task):
    """
    ASP-FOR-MI task
    
    Use aspirin to prevent myocardial infarction
    
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
        self.few_shot = self.config[TASK_ASP_FOR_MI]['few_shot']
        self.config[TASK_ASP_FOR_MI]['few_shot'] = self.few_shot
        
        aspirin_list_file = self.config[TASK_ASP_FOR_MI]['resources']['aspirin_file']
        self.aspirin_list = [e.strip() for e in open(aspirin_list_file, 'r').readlines()]
        
    def get_task_name(self):
        """
        Returns
        -------
        task_name: str
            The official name of the classification task performed by this plugin.
        """
        return TASK_ASP_FOR_MI
        
    def get_task_classes(self):
        """
        Returns
        -------
        The default class corresponding to this classification task.
        """
        return ["met", "not met"]
        
    def get_default_class(self):
        """
        Returns
        -------
        The default class corresponding to this classification task.
        """
        return "not met"
        
    
    
    def __call__(self, text_id, text, retriever, fastchat, preamble_type):
        """
        ASP-FOR-MI
        Use of aspirin to prevent MI
        """
        # Passage retrieval
        task_query = self.aspirin_list
        
        sentences = [s for s, _, _ in regex_sentencize(text)]
        sorted_kept_passages = retriever.get_best_passages((text_id, sentences),
                                                           (TASK_ASP_FOR_MI, task_query),
                                                           max_passages=5,
                                                           elbow_cutoff=True,
                                                           reset=True, logger=self.logger)

        abstract = ""
        for i, passage in enumerate(sorted_kept_passages['passages']):
            abstract += '    ' + passage.strip() + "\n\n"

        if self.few_shot:        
            preamble = asp_for_mi_2018_examples.example_dictionary[preamble_type]
            fastchat.init_conversation(preamble)
            
            if self.logger is not None:
                self.logger.debug(f"The preamble conversation for {TASK_ASP_FOR_MI} is " + '\n'.join(preamble))
            
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

Question: Does the text mention that the patient uses aspirin to prevent myocardial infarction (MI)?
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
            if answer.startswith('yes'):
                answer = "met"
            else:
                answer = "not met"

            return answer
    