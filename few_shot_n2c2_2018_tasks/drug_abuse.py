from data_utils import regex_sentencize
from task import n2c22018Task, register_task
from few_shot_prompts import drug_abuse_2018_examples

TASK_DRUG_ABUSE = 'DRUG-ABUSE'

@register_task(name='DRUG-ABUSE')
class DrugAbuse(n2c22018Task):
    """
    DRUG-ABUSE

    The patient abuses drugs (based on the train data, recreational marijuana is considered as a drug abuse)
    
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
        self.reset_every_sentence = self.config[TASK_DRUG_ABUSE]['reset_every_sentence']
        self.few_shot = self.config[TASK_DRUG_ABUSE]['few_shot']
        
    def get_task_name(self):
        """
        Returns
        -------
        task_name: str
            The official name of the classification task performed by this plugin.
        """
        return TASK_DRUG_ABUSE
        
    def get_default_class(self):
        """
        Returns
        -------
        The default class corresponding to this classification task.
        """
        return "not met"

    def get_task_classes(self):
        """
        Returns
        -------
        The default class corresponding to this classification task.
        """
        return ["not met", "met"]
            
    def __call__(self, text_id, text, retriever, fastchat, preamble_type):
        """
        DRUG-ABUSE

        The patient abuses drugs (based on the train data, recreational marijuana is considered as a drug abuse)
        """
    
        # Passage retrieval
        task_query = ["drug"]
        
        sentences = [s for s, _, _ in regex_sentencize(text)]

        sorted_kept_passages = retriever.get_best_passages((text_id, sentences),
                                                           (TASK_DRUG_ABUSE, task_query),
                                                           max_passages=5,
                                                           elbow_cutoff=True,
                                                           reset=True, logger=self.logger)

        abstract = ""
        for i, passage in enumerate(sorted_kept_passages['passages']):
            abstract += '    ' + passage.strip() + "\n\n"

        if self.few_shot:        
            preamble = drug_abuse_2018_examples.example_dictionary[preamble_type]
            fastchat.init_conversation(preamble)
            
            if self.logger is not None:
                self.logger.debug(f"The preamble conversation for {TASK_DRUG_ABUSE} is " + '\n'.join(preamble))
            
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

Question: Does the text mention that the patient used illicit drugs in the past?
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