prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has obesity? Answer Yes, No, Maybe, or Unmentioned to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "Bechman ( nephrology ) for further titration of her medications as needed. 8. Diabetes: The patient was initially continued on home dose"
    """.strip(),
    "Answer: The text does not mention if the patient has obesity. So the answer is Unmentioned.",
    '''
    Context: "PAST MEDICAL HISTORY: 1. Chronic hypertension. 2. Hypothyroidism. 3. Hypercholesterolemia. 4. Obesity. 5. Diabetes type II."
    '''.strip(),
    "Answer: The text mentions that the patient has obesity. So the answer is Yes.",
    '''
    Context: "53 yo female with DM , HTN , s/p MI 1980 , presenting with crescendo angina and hypertension."
    '''.strip(),
    "Answer: The text does not mention if the patient has obesity. So the answer is Unmentioned.",
    '''
    Context: "He had no history of diabetes or previous hypertension."
    '''.strip(),
    "Answer: The text does not mention if the patient has obesity. So the answer is Unmentioned.",
    '''
    Context: "CHF , coronary artery disease , diabetes , peripheral vascular disease , and chronic renal insufficiency that was admitted on 2/12/06 for weakness and confusion."
    '''.strip(),
    "Answer: The text does not mention if the patient has obesity. So the answer is Unmentioned.",
    '''
    Context: "October of 1998 , congestive heart failure with an ejection fraction of 45% , hypertension , diabetes mellitus , paroxysmal atrial fibrillation , hyperthyroidism , bilateral retinal detachment , status post left cataract surgery , status post appendectomy , status post cholecystectomy."
    '''.strip(),
    "Answer: The text does not mention if the patient has obesity. So the answer is Unmentioned.",
]

example_dictionary = {
    "example_A": example_A
}