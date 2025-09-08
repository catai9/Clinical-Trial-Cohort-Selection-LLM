prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has obstructive sleep apnea (OSA)? Answer Yes, No, Maybe, or Unmentioned to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "Several weeks ago and again the day of admission , she has had two-pillow orthopnea and paroxysmal nocturnal dyspnea."
    """.strip(),
    "Answer: The text does not mention if the patient has obstructive sleep apnea (OSA). So the answer is Unmentioned.",
    '''
    Context: "Significant for COPD , CHF , CAD , non-insulin-dependent diabetes mellitus , renal insufficiency , chronic venostasis , cellulitis , obesity , gout , sleep apnea , asthma , hypertension , urinary retention , degenerative joint disease of the right knee."
    '''.strip(),
    "Answer: The text mentions that the patient has sleep apnea. So the answer is Yes.",
    '''
    Context: "It is possible that she has sleep apnea given her body habitus and this would warrant follow-up as an outpatient."
    '''.strip(),
    "Answer: The text mentions that it is possible that the patient has obstructive sleep apnea (OSA). So the answer is Maybe.",
    '''
    Context: "Overnight pulse oximetry revealed no desaturations and there is a very low probability of sleep apnea despite habitus and a low probability based on her history."
    '''.strip(),
    "Answer: The text mentions that the patient does not have obstructive sleep apnea (OSA). So the answer is No.",
    '''
    Context: "DDx: arrythmia vs obstructive sleep apnea vs vasovagal episode YOu have also been referred for an outpatient sleep study to evaluate your obstructive sleep apnea."
    '''.strip(),
    "Answer: The text mentions that the patient might have obstructive sleep apnea (OSA) and needs an outpatient sleep study to evaluate it. So the answer is Maybe.",
    '''
    Context: "PMH:CAD , ppm for SSS , DMII , OSA , CPAP , HTN , gout , AAA repair , s/p choly"
    '''.strip(),
    "Answer: The text mentions that the patient has sleep apnea. So the answer is Yes.",
    '''
    Context: "PMH: adrenal adenoma , morbid obesity c/b OSA , OA c/b bilat THRs , R TKR ,"
    '''.strip(),
    "Answer: The text mentions that the patient has sleep apnea. So the answer is Yes.",
    '''
    Context: "HYPERTENSION. PAST MEDICAL HISTORY: Hospitalization for an episode of chest pain in S , hypertension and history of peripheral vascular disease with claudication symptoms."
    '''.strip(),
    "Answer: The text does not mention if the patient has obstructive sleep apnea (OSA). So the answer is Unmentioned.",
]

example_dictionary = {
    "example_A": example_A
}