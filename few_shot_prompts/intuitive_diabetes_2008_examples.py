prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has diabetes (DM)? Answer Yes, No, or Unsure to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "PMHx: notable for colonic strictures , DVT s/p IVC filter , ?DM , HTN ,"
    """.strip(),
    "Answer: The text has a question mark in front of DM. It is unclear if the patient has diabetes from the question mark. So the answer is Unsure.",
     '''
    Context: "62yo M with h/o morbid obesity , HTN , Afib ( not anticoagulated ) who presented to Pointden University Of Health Center on 4/29/02 complaining of signigicant rectal bright red blood per rectum , weakness , lightheadedness , and diaphoresis."
    '''.strip(),
    "Answer: The text does not mention that the patient has diabetes (DM). So the answer is No.",
    '''
    Context: "complicated by in-stent thrombosis ?3 years ago ) , HTN , DM ( hba1c 6.2 ) ,"
    '''.strip(),
    "Answer: The text mentions that the patient has diabetes (DM). So the answer is Yes.",
    '''
    Context: "*ENDO: questionable h/o DM."
    '''.strip(),
    "Answer: The text mentions questionable history of DM. It is unclear if the patient has diabetes from the question mark. So the answer is Unsure.",
]

example_dictionary = {
    "example_A": example_A
}