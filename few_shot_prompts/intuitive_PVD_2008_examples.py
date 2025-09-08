prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has peripheral vascular disease (PVD)? Answer Yes, No, or Unsure to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "HOSPITAL COURSE: 1 ) CV: Ischemia: Given the patient's cardiac history , she was admitted for a ROMI."
    """.strip(),
    "Answer: The text does not mention that the patient has peripheral vascular disease (PVD). So the answer is No.",
    '''
    Context: "Elective cardiac catheterization Was performed today for her annual post cardiac transplant evaluation revealed double vessel disease proximal LAD 95% lesion , LeftnCX ( Proximal ) , 75% lesion CX ( Mid ) , 95% lesion , MARG1 ( Ostial ) , 95% lesion . Successful PTCA/Stenting - LAD using XB3.5guide ,"
    '''.strip(),
    "Answer: The text does not mention that the patient has peripheral vascular disease (PVD). So the answer is No.",
    '''
    Context: "CAD , HTN , hyperlipidemia , PVD , tinnitus , NIDDM , osteoarthritis"
    '''.strip(),
    "Answer: The text mentions that the patient has peripheral vascular disease (PVD). So the answer is Yes.",
    '''
    Context: "However , cardiac enzymes are negative and an adenosine stress MIBI done on 8/27 was negative for ischemia and showed normal LV function. OTHER DIAGNOSIS;Conditions , Infections , Complications , affecting Treatment/Stay r/o mi ( R/O myocardial infarction ) disk herniation ( herniated disc ) hypercholesterolemia ( elevated cholesterol )"
    '''.strip(),
    "Answer: The text mentions that the patient has a negative stress test for ischemia but a history of past MI (Myocardial Infarction). It is possible that the MI is caused by peripheral vascular disease (PVD) but the text does not explicitly mention that the patient has peripheral vascular disease (PVD). So the answer is Unsure.",
    '''
    Context: "On exam , patient was noted to have positive jugular venous distension , 3/6 systolic murmur at the left upper sternal border , right lower quadrant tenderness to palpation , abdomen soft and without rebound tenderness."
    '''.strip(),
    "Answer: The text does not mention that the patient has peripheral vascular disease (PVD). So the answer is No.",
    '''
    Context: "A cardiac catheterization on 10/17/94 showed preliminary results of 80% stenosis in mid RCA which was successfully dilated to 20% with PTCA , an occluded LAD , an occluded"
    '''.strip(),
    "Answer: The text does not mention that the patient has peripheral vascular disease (PVD). So the answer is No.",
]

example_dictionary = {
    "example_A": example_A
}