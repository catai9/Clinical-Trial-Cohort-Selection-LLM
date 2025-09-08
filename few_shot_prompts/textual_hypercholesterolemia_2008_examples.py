prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has hypercholesterolemia? Answer Yes, No, Maybe, or Unmentioned to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "Her aspirin and statin were continued."
    """.strip(),
    "Answer: The text does not mention if the patient has hypercholesterolemia. So the answer is Unmentioned.",
    '''
    Context: "His cardiac risk factors include a history of cigarette smoking , hypertension , family history , questionable history of hypercholesterolemia and no history of diabetes."
    '''.strip(),
    "Answer: The text mentions that the patient has a questionable history of hypercholesterolemia. So the answer is Maybe.",
    '''
    Context: "PMH: esrd on HD ( MWF ) , DM , HTN , hyperchol , CAD ( 10/7 , PDA stent ) , CHF ( EF 50% , cLVH , inf hk ( 10/5 ) ) , gastritis , obesity , osa , bipolar , MSSA , C. diff ( 11/3 ) , nephrotic syndrome , sciatica/spinal
    "
    '''.strip(),
    "Answer: The text mentions that the patient has hyperchol. Hyperchol is another name for hypercholesterolemia. So the answer is Yes.",
    '''
    Context: "Cardiac risk factors include no family history , no diabetes , no hypercholesterolemia , very distant smoking history , male , and no hypertension."
    '''.strip(),
    "Answer: The text mentions that the patient does not have hypercholesterolemia. So the answer is No.",
    '''
    Context: "Includes chronic venous stasis ulcers in lower extremities , diabetes mellitus , hypertension , asthma , sarcoid , restricted pulmonary disease , and obesity."
    '''.strip(),
    "Answer: The text does not mention if the patient has hypercholesterolemia. So the answer is Unmentioned.",
    '''
    Context: "ASSOCIATED DIAGNOSES: 1. Congestive heart failure. 2. Hypertension. 3. Hypothyroidism."
    '''.strip(),
    "Answer: The text does not mention if the patient has hypercholesterolemia. So the answer is Unmentioned.",
    '''
    Context: "HTN , COPD , AAA repair , MI X 2 , multiple UTIs , CAP , elevated cholesterol"
    '''.strip(),
    "Answer: The text mentions that the patient has elevated cholesterol. Elevated cholesterol is another term for hypercholesterolemia. So the answer is Yes.",
]

example_dictionary = {
    "example_A": example_A
}