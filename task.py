from fastchat.model import load_model, get_conversation_template, add_model_args
from fastchat.utils import is_partial_stop, is_sentence_complete, get_context_length
from fastchat.model.model_adapter import load_model, get_conversation_template, get_generate_stream_function

from data_utils import regex_sentencize
from abc import ABC, abstractmethod

from datetime import datetime
import regex
import importlib

from os.path import join
from os import listdir

TASK_REGISTRY = {}

class NameConflictError(BaseException):
    """
    Raise for errors in adding plugins (tasks) due to the same name.
    """

def register_task(name):
    """
    Register an instantiated task to the TASK_REGISTRY dict.
    The tasks must be classes inheriting Task and must 
    be decorated by @register_task.
    (see "tasks" directory)
    """
    def wrapper_register_plugin(task_class):
        if name in TASK_REGISTRY and task_class.__name__ != TASK_REGISTRY[name].__name__:
            raise NameConflictError(
                f"Plugin name conflict: '{name} ({TASK_REGISTRY})'. Double check" \
                 " that all plugins have unique names.")
        
        assert issubclass(task_class, Task), f"{task_class} must inherit Task"
        TASK_REGISTRY[name] = task_class
        return task_class 

    return wrapper_register_plugin


def import_modules(dir_name):
    """
    Import all modules inside a directory.
    This way, we can just add a new file with new tasks, it will be imported
    without any further change of the main code
    """
    direc = dir_name
    for f in listdir(direc):
        path = join(direc, f)
        if (
            not f.startswith('_') 
            and not f.startswith('.') 
            and f.endswith('.py')
        ):
            file_name = f[:f.find('.py')]
            module = importlib.import_module(
                f'{dir_name}.{file_name}')


class Task(ABC):
    @abstractmethod
    def __call__(self, text_id, text, retriever, fastchat):
        ...
        
    @abstractmethod
    def get_task_name(self):
        """
        Returns
        -------
        task_name: str
            The official name of the classification task performed by this plugin.
        """
        ...
        
    @abstractmethod
    def get_default_class(self):
        """
        Returns
        -------
        The default class corresponding to this classification task.
        """
        ...        

    @abstractmethod
    def get_task_classes(self):
        """
        Returns
        -------
        classes: list of str
            All classes of the classification task performed by this plugin.
        """
        ...
        

class n2c22018Task(Task):
    def __init__(self, config):
        self.logger = config['logger'] if 'logger' in config else None
        self.config = config
        #self.tasks = {
        #    drug_abuse.TASK_DRUG_ABUSE: {
        #        "prompt_func":self.get_drug_abuse,
        #        "default": "not met"
        #    },
        #    english.TASK_ENGLISH: {
        #        "prompt_func":self.get_english,
        #        "default": "met"
        #    },
        #    dietsupp.TASK_DIETSUPP_2MOS: {
        #        "prompt_func":self.get_diet_supp,
        #        "default": "not met"
        #    }
        #}
        
        ## Parameters for record spliting
        self.RECORD_SEPARATOR = "****************************************************************************************************"
        self.RECORD_DATE_PATTERN = regex.compile("^\s*Record [dD]ate: (\d\d\d\d-\d\d-\d\d)")
        self.RECORD_DATE_FORMAT = '%Y-%m-%d'
        
        ## Parameters for section spliting
        section_titles_file = config['general']['resources']['section_titles']
        section_titles = [regex.sub(':', ' ?:', t.strip()) for t in open(section_titles_file, 'r').readlines()]
        self.section_title_regex = regex.compile(r'^\s*(' + '|'.join(section_titles) + ')', regex.IGNORECASE)
          
        
    def split_sections(self, text):
        """
        The text must contain only one record (not a patient compilation of records)
        """
        section_title = ""
        current_section = ''
        MIN_NEWLINE_NUMBER = 3
        newline_number = 0
        for line in text.split('\n'):
            if len(line.strip()) == 0:
                newline_number += 1
                if newline_number >= MIN_NEWLINE_NUMBER:
                    current_section = current_section.strip()
                    if len(current_section):
                        yield {"title":section_title, "text":current_section}
                    section_title = ""
                    current_section = ""
                else:
                    current_section += line + "\n"
            else:
                newline_number = 0
                
                matcher = self.section_title_regex.match(line)
                if matcher is not None:
                    current_section = current_section.strip()
                    if len(current_section):
                        yield {"title":section_title, "text":current_section}
                    current_section = line + '\n'
                    section_title = matcher.group(1)
                else:
                    current_section += line + '\n'
        if len(current_section.strip()):
            yield {"title":section_title, "text":current_section}
                
        
        
    def split_records(self, text):
        """
        The documents are made of several patient records, this function splits them
        and extract the date of the record when possible
        
        Returns: a list of tuples (date, text)
        """
        ## Split records
        record_texts = text.split(self.RECORD_SEPARATOR)
        ## Organizers say that number of records per patient is 2 to 5
        assert 3 <= len(record_texts) <= 6, '{} -> {} records'.format(index, len(records))   
        records = []
        ## Get record dates and save
        for (_record_index, record_text) in enumerate(record_texts):
            if len(record_text.strip()) > 0:
                matcher = self.RECORD_DATE_PATTERN.match(record_text)
                if matcher is None:
                    record_date = "unknown_date"
                else:
                    record_date = datetime.strptime(matcher.group(1), self.RECORD_DATE_FORMAT)
                records.append((record_date, record_text))
        return records        
        
  