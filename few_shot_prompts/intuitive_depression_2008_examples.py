prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has depressive disorder (depression)? Answer Yes, No, or Unsure to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "CHF ( congestive heart failure ) cad ( coronary artery disease ) htn ( hypertension ) dm ( diabetes mellitus ) gerd ( gastroesophageal reflux disease ) hypothyroidism ( hypothyroidism ) mitral regurgitation ( 2 ) lung ca s/p lobectomy ( lung cancer ) endometrial ca s/p TAH/BSO ( endometrial cancer ) basal cell ca ( basal cell carcinoma ) CRI ( chronic renal dysfunction ) renal artery stenosis s/p"
    """.strip(),
    "Answer: The text does not mention that the patient has depressive disorder (depression). So the answer is No.",
    '''
    Context: "He had two depressions infralaterally and was seen at CIMMC with question of restenosis."
    '''.strip(),
    "Answer: The text does not mention that the patient has depressive disorder (depression). So the answer is No.",
    '''
    Context: "Importance of both stressed and patient understands! SL TNG prn chest pain."
    '''.strip(),
    "Answer: The text does not mention that the patient has depressive disorder (depression). So the answer is No.",
    '''
    Context: "7. Psych: The patient has a history of depression."
    '''.strip(),
    "Answer: The text mentions that the patient has a history of depression. So the answer is Yes.",
    '''
    Context: "HISTORY OF PRESENT ILLNESS: Mr."
    '''.strip(),
    "Answer: The text does not mention that the patient has depressive disorder (depression). So the answer is No.",
    '''
    Context: "HTN DEPRESSION OBESITY TAH/BSO PRN Anxiety"
    '''.strip(),
    "Answer: The text mentions that the patient has a history of depression. So the answer is Yes.",
]

example_dictionary = {
    "example_A": example_A
}