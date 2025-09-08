from data_utils import regex_sentencize
from task import n2c22018Task, register_task
from few_shot_prompts import intuitive_PVD_2008_examples

TASK_INTUITIVE_PVD = 'intuitive_PVD'

@register_task(name='intuitive_PVD')
class IntuitivePVD(n2c22018Task):
    """
    intuitive_PVD
    
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
        self.few_shot = self.config[TASK_INTUITIVE_PVD]['few_shot']

    def get_task_name(self):
        """
        Returns
        -------
        task_name: str
            The official name of the classification task performed by this plugin.
        """
        return TASK_INTUITIVE_PVD
        
    def get_default_class(self):
        """
        Returns
        -------
        The default class corresponding to this classification task.
        """
        return 'Q'

    def get_task_classes(self):
        """
        Returns
        -------
        The default class corresponding to this classification task.
        """
        return ['Y', 'N', 'Q']
            
    def __call__(self, text_id, text, retriever, fastchat, preamble_type):
        """
        intuitive_PVD
        """
    
        # Passage retrieval
        task_query = ["PVD", "peripheral", "vascular"]
        
        sentences = [s for s, _, _ in regex_sentencize(text)]

        sorted_kept_passages = retriever.get_best_passages((text_id, sentences),
                                                           (TASK_INTUITIVE_PVD, task_query),
                                                           max_passages=5,
                                                           elbow_cutoff=True,
                                                           reset=True, logger=self.logger)

        abstract = ""
        for i, passage in enumerate(sorted_kept_passages['passages']):
            abstract += '    ' + passage.strip() + "\n\n"

        if self.few_shot:        
            preamble = intuitive_PVD_2008_examples.example_dictionary[preamble_type]
            fastchat.init_conversation(preamble)
            
            if self.logger is not None:
                self.logger.debug(f"The preamble conversation for {TASK_INTUITIVE_PVD} is " + '\n'.join(preamble))
            
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
            if answer.endswith('yes.') or answer.endswith('yes'):
                return 'Y'
            elif answer.endswith('no.') or answer.endswith('no'):
                return 'N'
            else:
                return 'Q'
        else:
            fastchat.reset_conversation()
            prompt = """
These are some sentences from a patient's clinical report. Answer Yes, No, or Unsure to the final question.  

{}

Question: Does the text mention that the patient has peripheral vascular disease (PVD)?
        """.format(abstract.rstrip()).strip()

            if self.logger is not None:
                self.logger.debug('-------------------\nPROMPT: ' + prompt)
            # Start at temperature 0 to allow reproductibility
            fastchat.set_gen_param("temperature", 0) 
            answer = fastchat.get_answer(prompt)['output']
            if self.logger is not None:
                self.logger.debug('\nANSWER: ' + answer)
            answer = answer.lower()
            if 'yes' in answer:
                return 'Y'
            elif 'no' in answer:
                return 'N'
            else:
                return 'Q'
        