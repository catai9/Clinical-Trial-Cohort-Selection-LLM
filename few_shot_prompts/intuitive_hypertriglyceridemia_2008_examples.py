prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has hypertriglyceridemia? Answer Yes, No, or Unsure to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "FAMILY HISTORY: Father with hypertension in his sixties , mother died of a vaginal cancer at a young age , daughter has asthma , and brother has hypertension."
    """.strip(),
    "Answer: The text does not mention that the patient has hypertriglyceridemia. So the answer is No.",
    '''
    Context: "LABORATORY DATA: His hematocrit was 47.4 , white cont 7.2 , platelets 241 , sodium 143 , potassium 4.2 , BUN 10 , creatinine 0.9 , glucose 213 , cholesterol 233 , triglycerides 278 , calcium 9.7 , albumen 4.4. All other labs were within normal limits."
    '''.strip(),
    "Answer: The text mentions that the patient has a triglyceride level of 278, which is above the normal triglyceride level. So the answer is Yes.",
    '''
    Context: "However , the patient experienced intermittent hypoglycemia at increased doses of Lantus and was returned to her home dose of 8 units subcu nightly."
    '''.strip(),
    "Answer: The text does not mention that the patient has hypertriglyceridemia. So the answer is No.",
    '''
    Context: "HTN ( hypertension ) h/o a.fib hypertriglyceride ( elevated lipids ) vertigo ( vertigo ) anxiety disorder"
    '''.strip(),
    "Answer: The text mentions that the patient has hypertriglyceride. So the answer is Yes.",
    '''
    Context: "HTN Dx`89 DM insulin dependent Dx `89 obesity ( obesity ) L knee DJD nephrotic syndrome 4/8 ( nephrotic syndrome ) hypercholesterolemia ( elevated cholesterol ) s/p medullary"
    '''.strip(),
    "Answer: The text does not mention that the patient has hypertriglyceridemia. So the answer is No.",
    '''
    Context: "CAD , HTN , hyperlipidemia , PVD , tinnitus , NIDDM , osteoarthritis"
    '''.strip(),
    "Answer: The text does not mention that the patient has hypertriglyceridemia. So the answer is No.",
    '''
    Context: "Fasting lipid profile on 3/18 revealed Triglycerides of 122 , HDL 28 ( low ) and normal cholesterol ( 122 ) , CLDL , VLDL"
    '''.strip(),
    "Answer: The text mentions that the patient has a triglyceride level of 278, which is within the normal triglyceride level. So the answer is No.",
]

example_dictionary = {
    "example_A": example_A
}