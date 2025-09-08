prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has gallstones? Answer Yes, No, Maybe, or Unmentioned to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "CLL status post fludarabine x4 cycles in 2004 in which has been stable with no evidence of residual or retroperitoneal lymphadenopathy , BPH , chronic kidney disease with a baseline
    creatinine of 2.5 , and glaucoma."
    """.strip(),
    "Answer: The text does not mention if the patient has gallstones. So the answer is Unmentioned.",
    '''
    Context: "CAD ( coronary artery disease ) CHF ( congestive heart failure ) diabetes ( diabetes mellitus type 2 ) renal transplant ( kidney transplant ) AAA repair ( abdominal aortic aneurysm ) open chole ( cholelithiasis ) hypertension ( hypertension )"
    '''.strip(),
    "Answer: The text mentions that the patient has cholelithiasis. Cholelithiasis is another term for gallstones. So the answer is Yes.",
    '''
    Context: "Abdominal ultrasound in the Emergency Room revealed right renal stones , but no hydronephrosis , no gallbladder stones , no evidence of triple A. "
    '''.strip(),
    "Answer: The text mentions that the patient does not have gallbladder stones. This means that the patient does not have gallstones. So the answer is No.",
    '''
    Context: "A/P: 88F w abd pain of unclear etiology on admission with transaminitis , abd pain and suspected bile duct stones and sludge."
    '''.strip(),
    "Answer: The text mentions that the patient has suspected bile duct stones. This means that the patient might have gallstones. So the answer is Maybe.",
    '''
    Context: "PSH: gastric bypass 15 of May , s/p cholecystectomy , bowel obstruction 2/1 total thyroidectomy 5/9"
    '''.strip(),
    "Answer: The text mentions that the patient has undergone cholecystectomy. Cholecystectomy is a surgical procedure to remove the gallbladder. So the answer is Yes.",
    '''
    Context: "October of 1998 , congestive heart failure with an ejection fraction of 45% , hypertension , diabetes mellitus , paroxysmal atrial fibrillation , hyperthyroidism , bilateral retinal detachment , status post left cataract surgery , status post appendectomy , status post cholecystectomy."
    '''.strip(),
    "Answer: The text mentions that the patient has undergone cholecystectomy. Cholecystectomy is a surgical procedure to remove the gallbladder. This means that the patient has had their gallbladder removed. So the answer is Yes.",
]

example_dictionary = {
    "example_A": example_A
}