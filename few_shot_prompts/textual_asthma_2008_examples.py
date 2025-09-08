prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has asthma? Answer Yes, No, Maybe, or Unmentioned to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "ALLERGIES were no known drug allergies."
    """.strip(),
    "Answer: The text does not mention if the patient has asthma. So the answer is Unmentioned.",
    '''
    Context: "FAMILY HISTORY: Father with hypertension in his sixties , mother died of a vaginal cancer at a young age , daughter has asthma , and brother has hypertension. PAST MEDICAL HISTORY: Negative for asthma , tuberculosis , or HIV risk factors."
    '''.strip(),
    "Answer: The text mentions that the patient's daughter has asthma. The text mentions that the patient is negative for asthma. So the answer is No.",
    '''
    Context: "Includes chronic venous stasis ulcers in lower extremities , diabetes mellitus , hypertension , asthma , sarcoid , restricted pulmonary disease , and obesity."
    '''.strip(),
    "Answer: The text mentions that the patient has asthma. So the answer is Yes.",
    '''
    Context: "PAST MEDICAL HISTORY: The patient's past medical history was significant for coronary artery disease , hypertension , hyperlipidemia , obesity , panic disorder , question of asthma , not on inhalers currently , gastroesophageal reflux disease , some his of rectal bleeding , but had a sigmoidoscope done in"
    '''.strip(),
    "Answer: The text mentions that there is a question of asthma for the patient. So the answer is Maybe.",
    '''
    Context: "ALLERGY: NKA"
    '''.strip(),
    "Answer: The text does not mention if the patient has asthma. So the answer is Unmentioned.",
    '''
    Context: "Pt. has a PROBABLE allergy to LISINOPRIL; reaction is ALLERGY: FLUORESCEIN DYE , TETRACYCLINE ANALOGUES , LISINOPRIL ,"
    '''.strip(),
    "Answer: The text does not mention if the patient has asthma. So the answer is Unmentioned.",
    '''
    Context: "MEDICATIONS UPON DISCHARGE: Tylenol 650 mg p.o. q.4h. p.r.n. headache; aspirin 81 mg p.o. daily; albuterol nebulizer 2.5 mg q.4h. p.r.n. shortness of breath or wheezing , of note , this is
    not the patient's usual medication , she does not have a history of asthma or COPD; Dulcolax 5 mg p.o. daily"
    '''.strip(),
    "Answer: The text mentions that the patient does not hvae a history of asthma. So the answer is No.",
    '''
    Context: "5 ) CHRONIC OBSTRUCTIVE PULMONARY DISEASE STATUS POST UNILATERAL"
    '''.strip(),
    "Answer: The text does not mention if the patient has asthma. So the answer is Unmentioned.",
]

example_dictionary = {
    "example_A": example_A
}