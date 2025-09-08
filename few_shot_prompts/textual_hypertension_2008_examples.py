prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has hypertension (HTN)? Answer Yes, No, Maybe, or Unmentioned to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "FAMILY HISTORY: Father with hypertension in his sixties , mother died of a vaginal cancer at a young age , daughter has asthma , and brother has hypertension."
    """.strip(),
    "Answer: The text mentions that the father and brother has hypertension. The text does not mention if the patient has hypertension. So the answer is Unmentioned.",
    '''
    Context: "1/25 chronic pancreatitis HTN"
    '''.strip(),
    "Answer: The text mentions that the patient has hypertension (HTN). So the answer is Yes.",
    '''
    Context: "The patient has no history of hypertension or tobacco use."
    '''.strip(),
    "Answer: The text mentions that the patient does not have hypertension (HTN). So the answer is No.",
    '''
    Context: "His mother , his brother , and his cousin and nephew all have the familial cardiomyopathy."
    '''.strip(),
    "Answer: The text does not mention if the patient has hypertension. So the answer is Unmentioned.",
    '''
    Context: "HISTORY OF PRESENT ILLNESS: This is a 55-year-old man with a history of smoking and a history of a left sided hemisphere stroke who was normotensive , nondiabetic and
    does not have known coronary disease who underwent a right-sided femoral to popliteal bypass graft in February of 1986 for severe claudication."
    '''.strip(),
    "Answer: The text mentions that the patient has normotensive. Normotensive means that the patient does not have hypertension (HTN). So the answer is No.",
    '''
    Context: "DISCHARGE DIAGNOSIS: CORONARY ARTERY DISEASE."
    '''.strip(),
    "Answer: The text does not mention if the patient has hypertension. So the answer is Unmentioned.",
]

example_dictionary = {
    "example_A": example_A
}