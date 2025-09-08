prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has atherosclerotic CV disease (CAD)? Answer Yes, No, or Unsure to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "Given the patient's history of atherosclerosis, further imaging of the abdominal vessels by MRA during followup was recommended by the GI Service."
    """.strip(),
    "Answer: The text does not mention that the patient has atherosclerotic CV disease (CAD). So the answer is No.",
    '''
    Context: "CV: CAD/ischemia: multiple CRF, past negative ETTs, sx unrelated to exertion but c/w angina otherwise (pressure/L arm paresthesia), with no assoc sx."
    '''.strip(),
    "Answer: The text mentions CAD but does not explicitly mention that the patient has atherosclerotic CV disease (CAD). It is unclear from the text if the patient has CAD. So the answer is Unsure.",
    '''
    Context: "Hospital Course: 75F with h/o CAD/CHF/lung CA/Afib with 3 days of weight gain, worsening SOB and orthopnea."
    '''.strip(),
    "Answer: The text mentions that the patient has a history of atherosclerotic CV disease (CAD). So the answer is Yes.",
    '''
    Context: "PAST MEDICAL HISTORY: Remarkable for rheumatic heart disease with mitral stenosis and mitral regurgitation, as well as aortic insufficiency and mild tricuspid insufficiency."
    '''.strip(),
    "Answer: The text does not mention that the patient has atherosclerotic CV disease (CAD). So the answer is No.",
    '''
    Context: "( H/O elevated cholesterol ) , htn ( hypertension ) , CAD s/p cabg"
    '''.strip(),
    "Answer: The text mentions that the patient has a history of atherosclerotic CV disease (CAD). So the answer is Yes.",
]

example_dictionary = {
    "example_A": example_A
}