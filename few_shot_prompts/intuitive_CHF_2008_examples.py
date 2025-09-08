prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has congestive heart failure (CHF)? Answer Yes, No, or Unsure to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "CAD , HTN , hyperlipidemia , PVD , tinnitus , NIDDM , osteoarthritis"
    """.strip(),
    "Answer: The text does not mention that the patient has congestive heart failure (CHF). So the answer is No.",
    '''
    Context: "He has congestive heart failure with last ejection fraction of 32% , hyperlipidemia , gout ,."
    '''.strip(),
    "Answer: The text mentions that the patient has congestive heart failure (CHF). So the answer is Yes.",
    '''
    Context: "Chest x-ray showing cardiomegaly and vascular congestion."
    '''.strip(),
    "Answer: The text mentions that the patient has vascular congestion. Vascular congestion is the first phase of congestive heart failure (CHF). So the answer is Yes.",
    '''
    Context: "He denied congestive heart failure and syncopal symptoms over the last few weeks."
    '''.strip(),
    "Answer: The text mentions that the patient does not have congestive heart failure (CHF). So the answer is No.",
    '''
    Context: "ABIs were obtained , which showed both left and right ABIs greater than 1 , also PVRs were normal throughout and it was felt that there was no vascular component to these nonhealing ulcers , and they recommended that it was due to venous stasis changes and chronic edema and felt local wound care and leg elevation would be the treatment of choice at this point."
    '''.strip(),
    "Answer: The text does not mention that the patient has congestive heart failure (CHF). So the answer is No.",
    '''
    Context: "His mother died of congestive heart failure at age 80. FAMILY HISTORY: His father died of coronary artery disease at age 48."
    '''.strip(),
    "Answer: The text does not mention that the patient has congestive heart failure (CHF). So the answer is No.",
]

example_dictionary = {
    "example_A": example_A
}