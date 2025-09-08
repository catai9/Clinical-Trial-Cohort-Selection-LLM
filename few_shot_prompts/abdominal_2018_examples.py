prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient a history of intra-abdominal surgery, intestine resection, or bowel obstruction? Answer Yes or No to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "- abdominal hernia"
    """.strip(),
    'Answer: The text mentions that the patient had abdominal hernia. Hernia is not considered part of intra-abdominal surgery, intestine resection, or bowel obstruction. So the answer is No.',
    """
    Context: "His bowel movements are regular. Abdomen is benign, soft, nontender, no masses, guarding,"
    """.strip(),
    'Answer: The text does not mention that the patient has a history of intra-abdominal surgery, intestine resection, or bowel obstruction. So the answer is No.',
    """
    Context: "Gastrointestinal: positive reflux"
    """.strip(),
    'Answer: The text does not mention that the patient has a history of intra-abdominal surgery, intestine resection, or bowel obstruction. So the answer is No.',
    """
    Context: "Procedures Hysterectomy"
    """.strip(),
    'Answer: The text mentions that the patient had hysterectomy procedure. Hysterectomy is a type of intra-abdominal surgery. So the answer is Yes.'
]

example_B = [prompt + 
    """
    Context: "Hysterectomy; Abdomen:  Soft, mildly overweight, non-distended, non-tender, no palpable pulsatile masses, no organomegaly, no abdominal bruit, no costovertebral tenderness"
    """.strip(),
    'Answer: The text mentions that the patient had hysterectomy. Hysterectomy is a type of intra-abdominal surgery. So the answer is Yes.',
    """
    Context: "Abdomen is benign, soft, nontender, no masses, guarding,"
    """.strip(),
    'Answer: The text does not mention that the patient has a history of intra-abdominal surgery, intestine resection, or bowel obstruction. So the answer is No.',
    """
    Context: "No change in bowel habits. Normoactive bowel sounds. Denies any abdominal pain. - abdominal hernia ABDOMEN:  Soft, nontender."
    """.strip(),
    'Answer: The text does not mention that the patient has a history of intra-abdominal surgery, intestine resection, or bowel obstruction. So the answer is No.',
    """
    Context: "Right inguinal hernia, referring to surgery."
    """.strip(),
    'Answer: The text mentions that the patient had a right inguinal hernia and underwent surgery for it. Inguinal hernia repair is a type of intra-abdominal surgery. So the answer is Yes.'
]

example_C = [prompt + 
    """
    Context: "About a year ago, she had an abdominal aortic aneurysm repair and in this setting developed some delirium and at that point was sent to rehab where she had a ankle"
    """.strip(),
    'Answer: The text mentions that the patient had an abdominal aortic aneurysm repair and underwent surgery for it. Abdominal aortic aneurysm repair is a type of intra-abdominal surgery. So the answer is Yes.',
    """
    Context: "He has no abdominal masses, tenderness or hepatosplenomegaly."
    """.strip(),
    'Answer: The text does not mention that the patient has a history of intra-abdominal surgery, intestine resection, or bowel obstruction. So the answer is No.',
    """
    Context: "Abd: soft, non-tender, non-distended. 8x8 cm mass like structure on right abdomen at rectus. Her abdomen is soft and nontender."
    """.strip(),
    'Answer: The text does not mention that the patient has a history of intra-abdominal surgery, intestine resection, or bowel obstruction. So the answer is No.',
    """
    Context: "Only operation is a total knee replacement on the left for arthritis and appendectomy."
    """.strip(),
    'Answer: The text mentions that the patient had an appendectomy in the past. Appendectomy is a type of abdominal surgery. So the answer is Yes.'
]

example_D = [prompt + 
    """
    Context: "No recent fever, no chills, no chest pain, no shortness of breath, no abdominal pain, no loss of bowel or bladder control, no unexplained weight loss."
    """.strip(),
    "Answer: The text does not mention that the patient has a history of intra-abdominal surgery, intestine resection, or bowel obstruction. So the answer is No.",
    """
    Context: "S/p appendectomy. Denies weight loss or gain, change in appetite, problems sleeping, night sweats, fevers, headaches, visual changes, dysphagia, shortness of breath, orthopnea, PND, chest pain, lower extremity edema, abdominal pain, nausea, vomiting, diarrhea, constipation, blood in stool, black stool, dysuria, nocturia, urinary or fecal incontinence, rashes, change in moles, joint pain, or depressed mood. no vaginal discharge, no pelvic pain, no dyspareunia."
    """.strip(),
    "Answer: The text mentions that the patient had an appendectomy, which is a type of abdominal surgery. So the answer is Yes.",
    """
    Context: "s/p cholecystectomy. He has no orthopnea, PND, abdominal distension, early satiety, abdominal pain or anorexia. -Chest:   Clear to percussion and ausculation. median sternotomy bandaged."
    """.strip(),
    'Answer: The text mentions that the patient had cholecystectomy, which is a type of intra-abdominal surgery. So the answer is Yes.',
    """
    Context: "KUB reviewed by me shows distended small bowel and. ABDOMEN:  Distended with absent bowel sounds, nontender. large bowel consistent with a large bowel obstruction versus an his abdominal distention, a KUB was done but there was no evidence; pain, shortness of breath, no abdominal pain, no cough, no fevers"
    """.strip(),
    'Answer: The text mentions that the patient has a distended small bowel and large bowel, which are consistent with a large bowel obstruction. So the answer is Yes.'
]

example_E = [prompt + 
    """
    Context: "Abdomen: No hepatosplenomegaly. Has had extensive laser in the past, and had some last year OS after her surgery. Ibarra, who has suggested surgery since a steroid injection did not help."
    """.strip(),
    "Answer: The text does not mention that the patient has a history of intra-abdominal surgery, intestine resection, or bowel obstruction. So the answer is No.",
    """
    Context: "No change in his bowel movements and no rectal bleeding. PROPHYLAXIS:    GI: none   DVT: fragmin    BOWEL: colace/senna   CODE:  FULL; He has had a small-bowel obstruction in the past as; Abdomen was soft and; Abdomen is soft and non tender."
    """.strip(),
    "Answer: The text mentions that the patient had a small-bowel obstruction in the past. So the answer is Yes.",
    """
    Context: "Abd: soft and non-tender without distension or rebound. normoactive bowel sounds, no organomegaly. No diarrhea, constipation, blood per rectum or melena."
    """.strip(),
    'Answer: The text does not mention that the patient has a history of intra-abdominal surgery, intestine resection, or bowel obstruction. So the answer is No.',
    """
    Context: "His past surgical history includes a resection of an aortic aneurysm in 2131, cholecystectomy in 2131, prostatectomy for cancer in 2142 and resection of a lung cancer in 2143."
    """.strip(),
    'Answer: The text mentions that the patient had a cholecystectomy in the past. Cholecystectomy is a type of intra-abdominal surgery. The text also mentions that the patient had a resection of an aortic aneurysm, prostatectomy for cancer, and resection of a lung cancer in the past. So the answer is Yes.'
]

vicuna_13b_fine_tuned = ["""Here are some sentences from a patient's clinical report. Does the text mention that the patient a history of intra-abdominal surgery, intestine resection, or bowel obstruction? Let's think step by step.""".strip() + "\n\n" + """
    Context: "- abdominal hernia"
    """.strip(),
    'Answer: The text mentions that the patient had abdominal hernia. Abdominal hernia is not intra-abdominal surgery, intestine resection, or bowel obstruction. So the answer is No.',
    """
    Context: "large bowel consistent with a large bowel obstruction versus an"
    """.strip(),
    'Answer: The text mentions that the patient had a large bowel obstruction. A large bowel obstruction is a type of bowel obstruction. So the answer is Yes.',
    """
    Context: "Lastly, as far as her ability to drive, this has been an issue for the last several months since her abdominal aortic aneurysm repair."
    """.strip(),
    'Answer: The text mentions that the patient had abdominal aortic aneurysm repair. So the answer is Yes.',
    """
    Context: "Abdomen was"
    """.strip(),
    'Answer: The text does not mention that the patient had intra-abdominal surgery, intestine resection, or bowel obstruction. So the answer is No.',
    """
    Context: "His bowel movements are regular."
    """.strip(),
    "Answer: The text mentions that the patient's bowel movements are regular. Regular bowel movements is not intra-abdominal surgery, intestine resection, or bowel obstruction. So the answer is No.",
    """
    Context: "Her abdomen is soft with positive bowel sounds."
    """.strip(),
    "Answer: The text mentions that the patient's abdomen is soft with positive bowel sounds. Positive bowel sounds is not intra-abdominal surgery, intestine resection, or bowel obstruction. So the answer is No.",
    """
    Context: "ROS: denies weight change, fever, chills, fatigue, blurry vision, chest pains, palpitations, dyspnea, cough, abdominal pain, nausea, vomiting, change in bowel/bladder habits, joint pain, dizziness, exanthem, edema."
    """.strip(),
    'Answer: The text mentions that the patient had abdominal pain and change in bowel/bladder habits. These are symptoms of bowel obstruction. So the answer is Yes.',
    """
    Context: "Lung cancer: s/p L partial resection"
    """.strip(),
    'Answer: The text mentions that the patient had partial resection, but does not state intestine resection. The text does not mention that the patient had intra-abdominal surgery, intestine resection, or bowel obstruction. So the answer is No.'
]

example_dictionary = {
    "example_A": example_A,
    "example_B": example_B,
    "example_C": example_C,
    "example_D": example_D,
    "example_E": example_E,
    "vicuna_13b_fine_tuned": vicuna_13b_fine_tuned
}