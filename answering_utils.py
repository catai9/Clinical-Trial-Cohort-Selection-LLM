import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig

from fastchat.model import load_model, get_conversation_template, add_model_args
from fastchat.utils import is_partial_stop, is_sentence_complete, get_context_length
from fastchat.model.model_adapter import load_model, get_conversation_template, get_generate_stream_function

from os.path import join, isfile, exists
import pandas as pd

def stream_output(output_stream):
    pre = 0
    for outputs in output_stream:
        output_text = outputs["text"]
        output_text = output_text.strip().split(" ")
        now = len(output_text) - 1
        if now > pre:
            #print(" ".join(output_text[pre:now]), end=" ", flush=True)
            pre = now
    #print(" ".join(output_text[pre:]), flush=True)
    return " ".join(output_text)     


class FastChatInterface:
    def __init__(self, model_path, device_params, gen_params, debug=False):
        self.model_path = model_path
        self.device_params = device_params
        self.set_gen_params(gen_params)
        self.debug = debug
        
        # Model
        self.model, self.tokenizer = load_model(
            model_path,
            device=device_params['device'],
            num_gpus=device_params['num_gpus'],
            #max_gpu_memory=max_gpu_memory,
            load_8bit=device_params['load_8bit'],
            #cpu_offloading=cpu_offloading,
            #gptq_config=gptq_config,
            #awq_config=awq_config,
            #revision=revision,
            debug=debug
        )
        self.generate_stream_func = get_generate_stream_function(self.model, self.model_path)
        self.context_len = get_context_length(self.model.config)
        self.conv = get_conversation_template(self.model_path)

    def reset_conversation(self):
        self.conv = get_conversation_template(self.model_path)
        
    def set_gen_param(self, key, value):
        self.gen_params[key] = value
        
    def set_gen_params(self, gen_params):
        self.gen_params = gen_params
        
    
    def init_conversation(self, conversation):
        """
        Parameters
        ----------
        conversation: str or list
            If str, conversation is a single question that the model must answer
            If list, conversation is a list of questions and answers. List size must be an even number 
            (n pairs of questions and answers)
        
        """
        self.reset_conversation()
        if type(conversation) == str:
            conversation = [conversation]
        assert len(conversation) % 2 == 0
        for i in range(0, len(conversation) - 1, 2):
            self.conv.append_message(self.conv.roles[0], conversation[i])
            self.conv.append_message(self.conv.roles[1], conversation[i+1])
        


    def get_answer(self, conversation, check_context_length=True, logger=None):
        """
        Parameters
        ----------
        conversation: str or list
            If str, conversation is a single question that the model must answer
            If list, conversation is a list of questions and answers. List size must be a odd number 
            (n pairs of questions and answers, then a question)
        check_context_length: bool, default True
            If true, raise ValueError of the provided context is longer than what the model is able to handle
        logger: Logger or None
        
        Returns
        -------
        answer: str
            The final answer 
        """
        if type(conversation) == str:
            conversation = [conversation]
        # List size must be a odd number 
        # (n pairs of questions and answers, then a question)
        assert len(conversation) % 2 == 1
        
        # Check context length
        if check_context_length:
            inputs = self.tokenizer(" ".join(conversation)) #, return_tensors="pt").to(model.device)
            input_ids = inputs["input_ids"]
            if logger is not None:
                logger.debug(f'Prompt length: {len(input_ids)}')
            if len(input_ids) > self.context_len:
                print(f'Prompt length: {len(input_ids)}, max: {self.context_len}')
                input_ids = input_ids[:self.context_len]
                # raise ValueError(f'Prompt length: {len(input_ids)}, max: {self.context_len}')
        
        
        model_type = str(type(self.model)).lower()
        is_t5 = "t5" in model_type
        # Hardcode T5's default repetition penalty to be 1.2
        if is_t5 and self.gen_params['repetition_penalty'] == 1.0:
            self.gen_params['repetition_penalty'] = 1.2
        # Set context length

        for i in range(0, len(conversation) - 1, 2):
            self.conv.append_message(self.conv.roles[0], conversation[i])
            self.conv.append_message(self.conv.roles[1], conversation[i+1])
            
        self.conv.append_message(self.conv.roles[0], conversation[-1])
        self.conv.append_message(self.conv.roles[1], None)

        prompt = self.conv.get_prompt()
        
        self.gen_params.update({
            "model": self.model_path, 
            "prompt": prompt,
            "stop": self.conv.stop_str,
            "stop_token_ids": self.conv.stop_token_ids,
        })
        
        output_stream = self.generate_stream_func(
            self.model,
            self.tokenizer,
            self.gen_params,
            self.device_params['device'],
            context_len=self.context_len,
            judge_sent_end=self.gen_params['judge_sent_end'],
        )
        outputs = stream_output(output_stream)
        self.conv.update_last_message(outputs.strip())
        return {
            "output":outputs,
            "prompt":prompt
        }