# ALL SMOKER CLASSES
prompt = """These are some sentences from a patient's clinical report. Classify the patient as Current Smoker, Non-Smoker, Past Smoker, Smoker (unsure if current or past smoker), or Unknown. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "Echocardiogram at Abrat Hospital showed left ventricular wall motion abnormalities with anteroapical aneurysm , EF of 20% , mild left atrial dilatation , aorticsclerosis and mild pulmonary hypertension ."
    """.strip(),
    "Answer: The text does not mention the patient's smoking habits. So the answer is Unknown.",
    '''
    Context: "The patient denied using tobacco."
    '''.strip(),
    "Answer: The text mentions that the patient does not use tobacco. Tobacco is another word for smoking. So the answer is Non-Smoker.",
    '''
    Context: "Please attempt to quit smoking."
    '''.strip(),
    "Answer: The text mentions that the patient needs to quit smoking. This suggests that the patient is currently smoking. So the answer is Current Smoker.",
    '''
    Context: "HAS BEEN SMOKING APPROXIMATELY 10 CIGARETTES A DAY."
    '''.strip(),
    "Answer: The text mentions that the patient has been smoking. So the answer is Current Smoker.",
    '''
    Context: "The patient is an ex-smoker."
    '''.strip(),
    "Answer: The text mentions that the patient is an ex-smoker. So the answer is Past Smoker.",
    '''
    Context: "history of cigarette use , post menopausal , hypercholesterolemia ."
    '''.strip(),
    "Answer: The sentence \"history of cigarette use\" indicates that the patient has smoked cigarettes in the past or is currently smoking. The absence of information about the patient's current smoking status makes it unclear whether the patient is a current or past smoker. So the answer is Smoker.",
]

example_dictionary = {
    "example_A": example_A
}