prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has hypertriglyceridemia? Answer Yes, No, Maybe, or Unmentioned to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "SECONDARY DIAGNOSES: 2. UNSTABLE ANGINA 3. HYPERTENSION 4. HYPERCHOLESTEROLEMIA 5. STATUS POST CORONARY ARTERY"
    """.strip(),
    "Answer: The text does not mention if the patient has hypertriglyceridemia. So the answer is Unmentioned.",
    '''
    Context: "HDL 48/triglycerides 60"
    '''.strip(),
    "Answer: The text mentions that the patient has hypertriglyceridemia. So the answer is Yes.",
    '''
    Context: "OTHER DIAGNOSIS;Conditions , Infections , Complications , affecting Treatment/Stay severe right internal carotid artery stenosis non-small cell lung cancer , pancytopenia secondary to chemotherapy hypertension , dyslipidemia , type 2 diabetes mellitus epilepsy"
    '''.strip(),
    "Answer: The text does not mention if the patient has hypertriglyceridemia. So the answer is Unmentioned.",
    '''
    Context: "HYPERCHOL/HYPER TG"
    '''.strip(),
    "Answer: The text mentions that the patient has hyper TG. Hyper TG is another term for hypertriglyceridemia. So the answer is Yes.",
    '''
    Context: "HTN Dx`89 DM insulin dependent Dx `89 obesity ( obesity ) L knee DJD nephrotic syndrome 4/8 ( nephrotic syndrome ) hypercholesterolemia ( elevated cholesterol ) s/p medullary"
    '''.strip(),
    "Answer: The text does not mention if the patient has hypertriglyceridemia. So the answer is Unmentioned.",
    '''
    Context: "PAST MEDICAL HISTORY: Diabetes , hypertension , hypercholesterolemia , chronic DVTs with pulmonary embolism x two , CVA , left temporal in the setting of an"
    '''.strip(),
    "Answer: The text does not mention if the patient has hypertriglyceridemia. So the answer is Unmentioned.",
    '''
    Context: "Seizure d/o , DM , CHF , CAD , CABG , HTN COPD , Schizo-affecitve disorder , dyslipidemia Meds on"
    '''.strip(),
    "Answer: The text does not mention if the patient has hypertriglyceridemia. So the answer is Unmentioned.",
    '''
    Context: "SECONDARY DIAGNOSIS: 1. CORONARY ARTERY DISEASE. 2. DIABETES MELLITUS. 3. HYPERCHOLESTEROLEMIA."
    '''.strip(),
    "Answer: The text does not mention if the patient has hypertriglyceridemia. So the answer is Unmentioned.",
]

example_dictionary = {
    "example_A": example_A
}