prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has gastroesophageal reflux disease (GERD)? Answer Yes, No, Maybe, or Unmentioned to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "Reason , MAZE procedure , mitral valve repair , aspirin , goal INR , PTT , DVT prophylaxis."
    """.strip(),
    "Answer: The text does not mention if the patient has gastroesophageal reflux disease (GERD). So the answer is Unmentioned.",
    '''
    Context: "MEDICAL HISTORY was notable for chronic psoriasis , vertigo question transient ischemic attack , status post multiple excisions for basal cell skin carcinoma , history of hiatal  ernia with a question of reflux esophagitis , status post suprapubic prostatectomy for benign prostatic hypertrophy , status post herniorrhaphy , status post appendectomy , question of glucose intolerance diet controlled , status post right cataract surgery with lens implantation."
    '''.strip(),
    "Answer: The text mentions that the patient has a question of reflux esophagitis. Reflux eosphagitis is another name for gastroesophageal reflux disease (GERD). So the answer is Maybe.",
    '''
    Context: "***PMH: CAD , s/p CVA , DM w neuropathy; h/o dialysis in 2004; falls , HTN , hypothyroidism , GERD"
    '''.strip(),
    "Answer: The text mentions that the patient has gastroesophageal reflux disease (GERD). So the answer is Yes.",
    '''
    Context: "Denies reflux or GERD."
    '''.strip(),
    "Answer: The text mentions that the patient does not have gastroesophageal reflux disease (GERD). So the answer is No.",
    '''
    Context: "Calcified aorta and iliac. 3. CT abdomen ( 1/14/070 : 1bilateral infiltrates consistent with pneumonia , questionable mild diffuse small-bowel thickening , no appendicitis , no obstruction , no perforation , positive gallstones , positive gallbladder distension without wall thickening or pericholecystic fluid."
    '''.strip(),
    "Answer: The text does not mention if the patient has gastroesophageal reflux disease (GERD). So the answer is Unmentioned.",
    '''
    Context: "He is currently eating a regular low-fat , low-cholesterol diet and is on Nexium."
    '''.strip(),
    "Answer: The text does not mention if the patient has gastroesophageal reflux disease (GERD). So the answer is Unmentioned.",
    '''
    Context: "PRILOSEC ( OMEPRAZOLE ) 20 MG PO QD"
    '''.strip(),
    "Answer: The text does not mention if the patient has gastroesophageal reflux disease (GERD). So the answer is Unmentioned.",
]

example_dictionary = {
    "example_A": example_A
}