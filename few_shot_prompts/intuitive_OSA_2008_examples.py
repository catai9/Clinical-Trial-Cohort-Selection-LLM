prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has obstructive sleep apnea (OSA)? Answer Yes, No, or Unsure to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "PULM-Considered sleep apnea , but no acute issues."
    """.strip(),
    "Answer: The text mentions that the patient may have sleep apnea but it is unclear if the patient has obstructive sleep apnea (OSA). So the answer is Unsure.",
    '''
    Context: "U Sa Fre CONTINGENT UPON SNF/rehab"
    '''.strip(),
    "Answer: The text does not mention that the patient has obstructive sleep apnea (OSA). So the answer is No.",
    '''
    Context: "OTHER DIAGNOSIS;Conditions , Infections , Complications , affecting Treatment/Stay urinary tract infection obesity ( obesity ) type 2 DM ( diabetes mellitus ) ?OSA ( ? sleep apnea )"
    '''.strip(),
    "Answer: The text has a question mark in front of OSA. It is unclear from the question mark if the patient has or does not have obstructive sleep apnea (OSA). So the answer is Unsure.",
    '''
    Context: "OTHER DIAGNOSIS;Conditions , Infections , Complications , affecting Treatment/Stay dm ( diabetes mellitus ) htn ( hypertension ) sleep apnea ( sleep apnea ) gout ( gout ) depression"
    '''.strip(),
    "Answer: The text mentions that the patient has sleep apnea. So the answer is Yes.",
    '''
    Context: "Consider full PFTS , screen for sleep apnea , adjustment of diuresis regimen , and TTE w/ bubble if no improvement ,"
    '''.strip(),
    "Answer: The text mentions that the patient needs to be screened for sleep apnea but it is unclear if the patient has obstructive sleep apnea (OSA). So the answer is Unsure.",
    '''
    Context: "PMH: coronary artery disease for which she underwent coronary angioplasty and a two-vessel coronary bypass grafting procedure 15 years , diabetes mellitus , hyperlipidemia and hypertension , iron-deficient anemia requiring intermittent transfusions , rheumatoid arthritis for which she is on prednisone , lymphangiectasia , restless leg syndrome , reflux disease and hypothyroidism"
    '''.strip(),
    "Answer: The text does not mention that the patient has obstructive sleep apnea (OSA). So the answer is No.",
    '''
    Context: "Several weeks ago and again the day of admission , she has had two-pillow orthopnea and paroxysmal nocturnal dyspnea"
    '''.strip(),
    "Answer: The text does not mention that the patient has obstructive sleep apnea (OSA). So the answer is No.",
    '''
    Context: "He also takes Ambien at night p.r.n. for insomnia."
    '''.strip(),
    "Answer: The text does not mention that the patient has obstructive sleep apnea (OSA). So the answer is No.",
]

example_dictionary = {
    "example_A": example_A
}