prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has peripheral vascular disease (PVD)? Answer Yes, No, Maybe, or Unmentioned to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "PAST MEDICAL HISTORY: Hypertension , coronary artery disease with a cardiac catheterization in 9/30 showing a 100 percent left anterior descending occlusion and right coronary artery occlusions , both fed by collaterals , 40 percent obtuse marginal one lesion."
    """.strip(),
    "Answer: The text does not mention if the patient has peripheral vascular disease (PVD). So the answer is Unmentioned.",
    '''
    Context: "PVD s/p R 5th toe amputation"
    '''.strip(),
    "Answer: The text mentions that the patient has peripheral vascular disease (PVD). So the answer is Yes.",
    '''
    Context: "No history of coronary artery disease , diabetes , tuberculosis , hepatic or renal disease."
    '''.strip(),
    "Answer: The text does not mention if the patient has peripheral vascular disease (PVD). So the answer is Unmentioned.",
    '''
    Context: "Vascular surgery saw the patient and felt that as long as the patient's hematocrit stabilized , she would not need any surgical intervention."
    '''.strip(),
    "Answer: The text does not mention if the patient has peripheral vascular disease (PVD). So the answer is Unmentioned.",
    '''
    Context: "On exam , patient was noted to have positive jugular venous distension , 3/6 systolic murmur at the left upper sternal border , right lower quadrant tenderness to palpation , abdomen soft and without rebound tenderness."
    '''.strip(),
    "Answer: The text does not mention if the patient has peripheral vascular disease (PVD). So the answer is Unmentioned.",
    '''
    Context: "PAST MEDICAL AND SURGICAL HISTORY: Significant for hypertension , peripheral vascular disease , dyslipidemia , renal failure , peptic ulcer disease with history of upper GI bleed and anxiety
    disorder."
    '''.strip(),
    "Answer: The text mentions that the patient has peripheral vascular disease (PVD). So the answer is Yes.", 
    '''
    Context: "PAST MEDICAL HISTORY: Insulin dependent diabetes mellitus complicated by peripheral neuropathy and impotence."
    '''.strip(),
    "Answer: The text does not mention if the patient has peripheral vascular disease (PVD). So the answer is Unmentioned.",
]

example_dictionary = {
    "example_A": example_A
}