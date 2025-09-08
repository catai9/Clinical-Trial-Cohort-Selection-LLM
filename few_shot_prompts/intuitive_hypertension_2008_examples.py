prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has hypertension (HTN)? Answer Yes, No, or Unsure to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "FAMILY HISTORY: Father with hypertension in his sixties , mother died of a vaginal cancer at a young age , daughter has asthma , and brother has hypertension."
    """.strip(),
    "Answer: The text mentions that the patient's father and brother has hypertension. The text does not mention that the patient has hypertension (HTN). So the answer is No.",
    '''
    Context: "OTHER DIAGNOSIS;Conditions , Infections , Complications , affecting Treatment/Stay HTN , COPD , AAA repair , MI X 2 , multiple UTIs , CAP , elevated cholesterol"
    '''.strip(),
    "Answer: The text mentions that the patient has hypertension (HTN). So the answer is Yes.",
    '''
    Context: "In the past , the patient had suffered severe hypotension when such medications have been added."
    '''.strip(),
    "Answer: The text does not mention that the patient has hypertension (HTN). So the answer is No.",
    '''
    Context: "Given his potassium , which was always borderline low in the 33 or 35 range , we decided to increase his Aldactone dose to 25 mg b.i.d. , but given his underlying renal insufficiency , we have decreased his standing"
    '''.strip(),
    "Answer: The text does not mention that the patient has hypertension (HTN). So the answer is No.",
    '''
    Context: "This is a 55-year-old man with a history of smoking and a history of a left sided hemisphere stroke who was normotensive , nondiabetic and does not have known coronary disease who underwent a right-sided femoral to popliteal bypass graft in February of 1986 for severe
    claudication."
    '''.strip(),
    "Answer: The text does not mention that the patient has hypertension (HTN). So the answer is No.",
    '''
    Context: "DISCHARGE DIAGNOSIS: CORONARY ARTERY DISEASE."
    '''.strip(),
    "Answer: The text does not mention that the patient has hypertension (HTN). So the answer is No.",
]

example_dictionary = {
    "example_A": example_A
}