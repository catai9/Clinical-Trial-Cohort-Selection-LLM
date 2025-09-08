prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient does not speak English? Answer Yes or No to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "Xie send a paring for fungal culture before we consider it."
    """.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is No.",
    """
    Context: "Ultrasound showed what is being interpreted as a stable slightly enlarge intramammary lymph node."
    """.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is No.",
    '''
    Context: "In PVH ED, pt describes the pain as like a bleeding scar and states my heart is bloated through her daughter who acted as her interpreter.
    '''.strip(),
    "Answer: The text mentions that the patient's daughter acts as her interpreter. We can infer that the patient cannot speak English. So the answer is Yes.",
    '''
    Context: "Procedure:  The patient is a 56-year-old Spanish-speaking female scheduled for laparoscopic cholecystectomy."
    '''.strip(),
    "Answer: The text mentions that the patient speaks Spanish. We can infer that the patient cannot speak English. So the answer is Yes.",
    '''
    Context: "She speaks in a high-pitched somewhat hoarse voice."
    '''.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is No.",
    '''
    Context: Source: Chart and Pt.'s husband - Pt is non-verbal.
    '''.strip(),
    "Answer: The text mentions that the patient is non-verbal, does it does not mention explicitly that he cannot speak English. So the answer is No."
]

example_B = [prompt + 
    """
    Context: "Atlantic North so that I can communicate with him about the recent events and arrange for follow-up colonoscopy."
    """.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is No.",
    """
    Context: "speak with the patient chief complaint is weakness."
    """.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is No.",
    '''
    Context: "*H&P conducted with interpreter present."
    '''.strip(),
    "Answer: The text mentions that the history and physical exam (H&P) were conducted with an interpreter. We can infer that the patient cannot speak English. So the answer is Yes.",
    '''
    Context: "Fay is a 70 year old spanish speaking female with multiple medical problems who presents today as a follow up for her diabetes, adrenal insufficiency"
    '''.strip(),
    "Answer: The text mentions that the patient speaks Spanish. We can infer that the patient cannot speak English. So the answer is Yes.",
    '''
    Context: "She is a poor historian, accompanied by family members who interpret, both in Korean and English."
    '''.strip(),
    "Answer: The text mentions that the patient needs an interpreter to communicate. So the answer is Yes.",
    '''
    Context: "He is planning to return to work as a printing press operator."
    '''.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is No."
]

example_C = [prompt + 
    """
    Context: "She is dependent for all of her ADLs and has a home health aide."
    """.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is No.",
    """
    Context: "Former communications manager; currently works part time in securities"
    """.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is No.",
    '''
    Context: "She is a poor historian, accompanied by family members who interpret, both in Korean and English."
    '''.strip(),
    "Answer: The text mentions that the patient's family members interpreted for the patient. We can infer that the patient cannot speak English. So the answer is Yes.",
    '''
    Context: "Procedure:  The patient is a 71 year old Spanish-speaking female scheduled for right colectomy."
    '''.strip(),
    "Answer: The text mentions that the patient speaks Spanish. We can infer that the patient cannot speak English. So the answer is Yes.",
    '''
    Context: "Speech/Lang: 	difficult to assess since not cooperating with exam and drowsy.
    '''.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is No.",
    '''
    Context: "She is a vague historian, but has not had clear rest anginal symptoms."
    '''.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is No."
]

example_D = [prompt + 
    """
    Context: "Catheterization s/p transfer to HCC demonstrated diffuse native disease as well as complete occlusion of SVG and touchdown lesion of LIMA."
    """.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is No.",
    """
    Context: "Image interpretation reviewed by Dr."
    """.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is No.",
    """
    Context: "Source: Chart and Pt.'s husband - Pt is non-verbal"
    """.strip(),
    'Answer: The text makes no mention of the patient\'s language or the need for an interpreter to speak to the doctor. So the answer is No.',
    """
    Context: "*H&P conducted with interpreter present."
    """.strip(),
    'Answer: The text mentions that the history and physical exam (H&P) were conducted with an interpreter present. We can infer that the patient cannot speak English. So the answer is Yes.',
    """
    Context: "Fay is a 70 year old spanish speaking female with multiple medical problems who presents today as a follow up for her diabetes, adrenal insufficiency"
    """.strip(),
    'Answer: The text mentions that the patient speaks Spanish. We can infer that the patient cannot speak English. So the answer is Yes.',
    """
    Context: "Pt intermittenly responds to commands and is not speaking, so ROS is unabl to obtain at this point."
    """.strip(),
    'Answer: The text makes no mention of the patient\'s language or the need for an interpreter to speak to the doctor. So the answer is No.'
]

example_E = [prompt + 
    """
    Context: "For urgent problems or questions about your blood sugar or insulin call 387-8267 and ask for the page operator. The patient lives with his wife and son and is a retired Fire Chief."
    """.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is No.",
    """
    Context: "Speech fluent, spontaneous."
    """.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is No.",
    """
    Context: "Gen: pleasant elderly gentleman, trying to speak but is not understandable;"
    """.strip(),
    'Answer: The text makes no mention of the patient\'s language or the need for an interpreter to speak to the doctor. So the answer is No.',
    """
    Context: "Procedure:  The patient is a 56-year-old Spanish-speaking female scheduled for laparoscopic cholecystectomy."
    """.strip(),
    'Answer: The text mentions that the patient speaks Spanish and needs an interpreter to communicate. So the answer is Yes.',
    """
    Context: "Procedure:  The patient is a 71 year old Spanish-speaking female scheduled for right colectomy."
    """.strip(),
    'Answer: The text mentions that the patient speaks Spanish. We can infer that the patient cannot speak English. So the answer is Yes.',
    """
    Context: "She is a poor historian, accompanied by family members who interpret, both in Korean and English."
    """.strip(),
    'Answer: The text mentions that the patient needs an interpreter to communicate. So the answer is Yes.'
]

vicuna_13b_fine_tuned = ["""These are some sentences from a patient's clinical report. Does the patient speak English? Answer No, only if it is explicitly stated that the patient needs an interpreter, cannot speak at all or speaks a language other than English. Let's think step by step.

    Context: "Xie send a paring for fungal culture before we consider it."
    """.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is Yes.",
    """
    Context: "Ultrasound showed what is being interpreted as a stable slightly enlarge intramammary lymph node."
    """.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is Yes.",
    '''
    Context: "In PVH ED, pt describes the pain as like a bleeding scar and states my heart is bloated through her daughter who acted as her interpreter.
    '''.strip(),
    "Answer: The text mentions that the patient's daughter acts as her interpreter. We can infer that the patient cannot speak English. So the answer is No.",
    '''
    Context: "Procedure:  The patient is a 56-year-old Spanish-speaking female scheduled for laparoscopic cholecystectomy."
    '''.strip(),
    "Answer: The text mentions that the patient speaks Spanish. We can infer that the patient cannot speak English. So the answer is No.",
    '''
    Context: "She speaks in a high-pitched somewhat hoarse voice."
    '''.strip(),
    "Answer: The text makes no mention of the patient's language or the need for an interpreter to speak to the doctor. So the answer is Yes.",
    '''
    Context: Source: Chart and Pt.'s husband - Pt is non-verbal.
    '''.strip(),
    "Answer: The text mentions that the patient is non-verbal, does it does not mention explicitly that he cannot speak English. So the answer is Yes."
]

example_dictionary = {
    "example_A": example_A,
    "example_B": example_B,
    "example_C": example_C,
    "example_D": example_D,
    "example_E": example_E,
    "vicuna_13b_fine_tuned": vicuna_13b_fine_tuned
}