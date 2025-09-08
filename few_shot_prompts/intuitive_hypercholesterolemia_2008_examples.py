prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has hypercholesterolemia? Answer Yes, No, or Unsure to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "CAD , HTN , hyperlipidemia , PVD , tinnitus , NIDDM , osteoarthritis"
    """.strip(),
    "Answer: The text mentions that the patient has hyperlipidemia. Hypercholesterolemia is a type of hyperlipidemia. So the answer is Yes.",
    '''
    Context: "OTHER DIAGNOSIS;Conditions , Infections , Complications , affecting Treatment/Stay htn ( hypertension ) obesity ( obesity ) h/o sarcoid ( H/O sarcoid ) arthritis ( polyarticular  rthritis ) diverticulosis ( diverticulosis ) ventral hernia depression ( depression ) unstable angina ( angina )"
    '''.strip(),
    "Answer: The text does not mention that the patient has hypercholesterolemia. So the answer is No.",
    '''
    Context: "He is currently eating a regular low-fat , low-cholesterol diet and is on Nexium."
    '''.strip(),
    "Answer: The text does not mention that the patient has hypercholesterolemia. So the answer is No.",
    '''
    Context: "PAST MEDICAL HISTORY: Significant for hypercholesterolemia , pulmonary embolism in 1987 ,"
    '''.strip(),
    "Answer: The text mentions the patient has hypercholesterolemia. So the answer is Yes.",
    '''
    Context: "Given the patient's history of atherosclerosis , further imaging of the abdominal vessels by MRA during followup was recommended by the GI Service. 2. Pneumonia: Bilateral infiltrates consistent with aspiration pneumonia. PAST MEDICAL HISTORY: Hypertension , atrial fibrillation on"
    '''.strip(),
    "Answer: The text does not mention that the patient has hypercholesterolemia. So the answer is No.",
    '''
    Context: "IHSS and insulin dependent diabetes who now presented with a syncopal episode accompanied by substernal chest pressure."
    '''.strip(),
    "Answer: The text does not mention that the patient has hypercholesterolemia. So the answer is No.",
]

example_dictionary = {
    "example_A": example_A
}