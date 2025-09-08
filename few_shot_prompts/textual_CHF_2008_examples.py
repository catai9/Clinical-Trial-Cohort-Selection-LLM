prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has congestive heart failure (CHF)? Answer Yes, No, Maybe, or Unmentioned to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: " His cardiac history began in 26 of September , when he suffered a non-Q-wave myocardial infarction."
    """.strip(),
    "Answer: The text does not mention if the patient has congestive heart failure (CHF). So the answer is Unmentioned.",
    '''
    Context: "Recent signs and symptoms of congestive heart failure include dyspnea on exertion."
    '''.strip(),
    "Answer: The text mentions that the patient has congestive heart failure (CHF). So the answer is Yes.",
    '''
    Context: " However , he had no history of myocardial infarction or congestive heart failure."
    '''.strip(),
    "Answer: The text mentions that the patient does not have congestive heart failure (CHF). So the answer is No.",
    '''
    Context: "PMH: Coronary artery disease , CHF , echo in July of 1999 shows moderate left ventricular hypertrophy of about 65% , diabetes type 2 20 years including with retinopathy , nephropathy and neuropathic pain ,"
    '''.strip(),
    "Answer: The text mentions that the patient has congestive heart failure (CHF). So the answer is Yes.",
    '''
    Context: "AM enzymes pending. *PUMP: no evidence of volume overload , CHF."
    '''.strip(),
    "Answer: The text mentions that the patient does not have any evidence of congestive heart failure (CHF). So the answer is No.",
    '''
    Context: "Includes chronic venous stasis ulcers in lower extremities , diabetes mellitus , hypertension , asthma , sarcoid , restricted pulmonary disease , and obesity."
    '''.strip(),
    "Answer: The text does not mention if the patient has congestive heart failure (CHF). So the answer is Unmentioned.",
]

example_dictionary = {
    "example_A": example_A
}