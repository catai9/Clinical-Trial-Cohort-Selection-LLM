from data_utils import regex_sentencize
from task import n2c22018Task, register_task
from few_shot_prompts import textual_depression_2008_examples

TASK_TEXTUAL_DEPRESSION = 'textual_Depression'

@register_task(name='textual_Depression')
class TextualDepression(n2c22018Task):
    """
    textual_Depression
    
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
        self.few_shot = self.config[TASK_TEXTUAL_DEPRESSION]['few_shot']

    def get_task_name(self):
        """
        Returns
        -------
        task_name: str
            The official name of the classification task performed by this plugin.
        """
        return TASK_TEXTUAL_DEPRESSION
        
    def get_default_class(self):
        """
        Returns
        -------
        The default class corresponding to this classification task.
        """
        return 'U'

    def get_task_classes(self):
        """
        Returns
        -------
        The default class corresponding to this classification task.
        """
        return ['Y', 'N', 'Q', 'U']
            
    def __call__(self, text_id, text, retriever, fastchat, preamble_type):
        """
        textual_Depression
        """
    
        # Passage retrieval
        task_query = ["depression"]
        
        sentences = [s for s, _, _ in regex_sentencize(text)]

        sorted_kept_passages = retriever.get_best_passages((text_id, sentences),
                                                           (TASK_TEXTUAL_DEPRESSION, task_query),
                                                           max_passages=5,
                                                           elbow_cutoff=True,
                                                           reset=True, logger=self.logger)

        abstract = ""
        for i, passage in enumerate(sorted_kept_passages['passages']):
            abstract += '    ' + passage.strip() + "\n\n"

        if self.few_shot:  
            preamble = textual_depression_2008_examples.example_dictionary[preamble_type]
            fastchat.init_conversation(preamble)
            
            if self.logger is not None:
                self.logger.debug(f"The preamble conversation for {TASK_TEXTUAL_DEPRESSION} is " + '\n'.join(preamble))
            
            prompt = '''
    Context: "{}"
            '''.format(abstract).strip()
            
            answer = ''
            # Start at temperature 0 to allow reproductibility
            fastchat.set_gen_param("temperature", 0) 
            result = fastchat.get_answer(prompt, logger=self.logger)
            answer = result['output']

            if self.logger is not None:
                self.logger.debug('-------------------\nLINE: ' + abstract)
            
            if self.logger is not None:
                self.logger.debug("ANSWER: " + answer)
            
            answer = answer.lower()
            if answer.endswith('yes.') or answer.endswith('yes'):
                return 'Y'
            elif answer.endswith('no.') or answer.endswith('no'):
                return 'N'
            elif answer.endswith('maybe.') or answer.endswith('maybe'):
                return 'Q'
            else:
                return 'U'
        else:
            fastchat.reset_conversation()
            prompt = """
These are some sentences from a patient's clinical report. Answer Yes, No, Maybe, or Unmentioned to the final question. 

{}

Question: Does the text mention that the patient has depression?
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
            if 'yes' in answer:
                return 'Y'
            elif 'no' in answer:
                return 'N'
            elif 'maybe' in answer:
                return 'Q'
            else:
                return 'U'
        
        