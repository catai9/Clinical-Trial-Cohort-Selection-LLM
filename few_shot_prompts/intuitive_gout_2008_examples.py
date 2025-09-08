prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has gout? Answer Yes, No, or Unsure to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "PAST MEDICAL HISTORY: Past medical history was significant for high blood pressure , left ankle and left knee arthritis , questionable history of gout , gonococcal urethritis , diverticulosis , elevated cholesterol , and cardiomyopathy with ejection fraction of 35% by echocardiogram in September of 1998."
    """.strip(),
    "Answer: The text mentions that the patient has a questionable history of gout. So the answer is Unsure.",
    '''
    Context: "positive gallstones , positive gallbladder distension without wall thickening or pericholecystic fluid."
    '''.strip(),
    "Answer: The text does not mention that the patient has gout. So the answer is No.",
    '''
    Context: "The following medications were stopped during this admission given concern re: elevated LFT's , ARF , and guiaic (+) stools: tylenol, percocet, zocor, cozaar, celebrex, allopurinol, ASA."
    '''.strip(),
    "Answer: The text mentions \"guiaic (+) stools\" which refers to the presence of uric acid crystals in the patient's stool, which is a characteristic symptom of Gout. Additionally, the text also mentions that the patient has elevated liver function tests (LFTs) and acute renal failure (ARF), which are both associated with Gout. Therefore, the text suggests that the patient has Gout. So the answer is Yes.",
    '''
    Context: "h/o chronic renal insufficiency ( H/O chronic renal dysfunction ) , gout ( gout ) "
    '''.strip(),
    "Answer: The text mentions the patient has gout. So the answer is Yes.",
    '''
    Context: "PAST MEDICAL HISTORY: Hypertension , atrial fibrillation on"
    '''.strip(),
    "Answer: The text does not mention that the patient has gout. So the answer is No.",
    '''
    Context: "HISTORY OF PRESENT ILLNESS: This is a 75-year-old woman with a history of rheumatic heart disease , status post St."
    '''.strip(),
    "Answer: The text does not mention that the patient has gout. So the answer is No.",
]

example_dictionary = {
    "example_A": example_A
}