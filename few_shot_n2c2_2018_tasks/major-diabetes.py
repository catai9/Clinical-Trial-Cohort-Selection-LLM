from data_utils import regex_sentencize
from task import n2c22018Task, register_task
from few_shot_prompts import major_diabetes_2018_examples

TASK_MAJOR_DIABETES = 'MAJOR-DIABETES'

@register_task(name='MAJOR-DIABETES')
class MajorDiabetes(n2c22018Task):
    """
    MAJOR-DIABETES

    Major diabetes-related complication. For the purposes of this annotation, we define "major complication" (as opposed to "minor complication") as any of the following that are a result of (or strongly correlated with) uncontrolled diabetes:
    ○ Amputation
    ○ Kidney damage
    ○ Skin conditions
    ○ Retinopathy
    ○ Nephropathy
    ○ neuropathy
    
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
        self.few_shot = self.config[TASK_MAJOR_DIABETES]['few_shot']
        
    def get_task_name(self):
        """
        Returns
        -------
        task_name: str
            The official name of the classification task performed by this plugin.
        """
        return TASK_MAJOR_DIABETES
        
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
        MAJOR-DIABETES

        Major diabetes-related complication. For the purposes of this annotation, we define "major complication" (as opposed to "minor complication") as any of the following that are a result of (or strongly correlated with) uncontrolled diabetes:
            ○ Amputation
            ○ Kidney damage
            ○ Skin conditions
            ○ Retinopathy
            ○ Nephropathy
            ○ neuropathy
        """
    
        # Passage retrieval
        task_query = ["amputation", "kidney", "skin", "nephropathy", "neuropathy", "LUE", "retinal", "macular", "paresthesias", "eye", "vision", "renal", "ulcer", "UTI"]
        
        sentences = [s for s, _, _ in regex_sentencize(text)]

        sorted_kept_passages = retriever.get_best_passages((text_id, sentences),
                                                           (TASK_MAJOR_DIABETES, task_query),
                                                           max_passages=15,
                                                           elbow_cutoff=True,
                                                           reset=True, logger=self.logger)

        abstract = ""
        for i, passage in enumerate(sorted_kept_passages['passages']):
            abstract += '    ' + passage.strip() + "\n\n"

        if self.few_shot:
            preamble = major_diabetes_2018_examples.example_dictionary[preamble_type]
            fastchat.init_conversation(preamble)
            
            if self.logger is not None:
                self.logger.debug(f"The preamble conversation for {TASK_MAJOR_DIABETES} is " + '\n'.join(preamble))
            
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
You are a knowledgeable healthcare professional who has been tasked with identifying potential major diabetes-related complications from patient text records. These complications include amputation, kidney damage, skin conditions, retinopathy, nephropathy, neuropathy, and UTI. Please review the patient records provided below and determine if there are any mentions of these major complications. Only answer Yes if there is explicit mention of these major complications for the patient.

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
            if answer.startswith('yes'):
                answer = "met"
            else:
                answer = "not met"

            return answer
        