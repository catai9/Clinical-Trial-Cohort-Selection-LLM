prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has Gout? Answer Yes, No, Maybe, or Unmentioned to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "Osteoarthritis , Asthma , Type II Diabetes , Chronic Pain Syndrome ,"
    """.strip(),
    "Answer: The text does not mention if the patient has Gout. So the answer is Unmentioned.",
    '''
    Context: "PAST MEDICAL HISTORY: Past medical history was significant for high blood pressure , left ankle and left knee arthritis , questionable history of gout , gonococcal urethritis ,"
    '''.strip(),
    "Answer: The text mentions that the patient has a questionable history of Gout. So the answer is Maybe.",
    '''
    Context: "HPI: 80 F w/gout , OA s/p bilateral knee replacement in 1992 , admitted with acute on chronic R knee pain."
    '''.strip(),
    "Answer: The text mentions that the patient has Gout. So the answer is Yes.",
    '''
    Context: "Calcified aorta and iliac. 3. CT abdomen ( 1/14/070 : 1bilateral infiltrates consistent with pneumonia , questionable mild diffuse small-bowel thickening , no appendicitis , no obstruction , no perforation , positive gallstones , positive gallbladder distension without wall thickening or pericholecystic fluid."
    '''.strip(),
    "Answer: The text does not mention if the patient has Gout. So the answer is Unmentioned.",
    '''
    Context: "LGIB TOBACCO PAF-no anticoag for distant h/o lgi bleed htn dm hyperchol periph neuropathy h pylori"
    '''.strip(),
    "Answer: The text does not mention if the patient has Gout. So the answer is Unmentioned.",
    '''
    Context: "PMH: asthma , PSVT in 2001 , obesity , obstructive sleep apnea , thalessemia trait"
    '''.strip(),
    "Answer: The text does not mention if the patient has Gout. So the answer is Unmentioned.",
]

example_dictionary = {
    "example_A": example_A
}