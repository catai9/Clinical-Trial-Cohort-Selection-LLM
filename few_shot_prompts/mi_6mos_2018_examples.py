prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient recently had MI? Answer Yes or No to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "Cardiac etiology would be of greatest concern given hx of CAD and chest pain, though certainly cerebrovascular disease is present given CVA history."
    """.strip(),
    'Answer: The text does not mention that the patient had MI, NSTEMI, or STEMI. So the answer is No.',
    """
    Context: "45 yo F w/ h/o DM, HTN, hypertriglyceridemia, tobacco use p/w SSCP and inferior STEMI."
    """.strip(),
    'Answer: The text mentions that the patient had STEMI. So the answer is Yes.',
    """
    Context: "81 yo man with a history of DM2, HTN, CRI who presented with a NSTEMI and CHF."
    """.strip(),
    'Answer: The text mentions that the patient had NSTEMI. So the answer is Yes.',
    """
    Context: "Cardiac: Regular rate and rhythm."
    """.strip(),
    'Answer: The text does not mention that the patient had MI, NSTEMI, or STEMI. So the answer is No.',
]

example_B = [prompt + 
    """
    Context: "HISTORY OF PRESENT ILLNESS:  This is an elderly patient, 82, with known diabetes and coronary artery disease, which has required placement of a pacemaker."
    """.strip(),
    'Answer: The text does not mention that the patient had MI, NSTEMI, or STEMI. So the answer is No.',
    """
    Context: "Ischemia:  Has CRI, and just had a NSTEMI with a Troponin peak at 2.91 on 3/23, but now with an increase to 3.73."
    """.strip(),
    'Answer: The text mentions that the patient had NSTEMI. So the answer is Yes.',
    """
    Context: "PAST MEDICAL HISTORY:  Significant for the type I diabetes as described, her pernicious anemia, C6-C7 vertebral degenerative disease, pulmonary embolus and also some mild asthma in the past."
    """.strip(),
    'Answer: The text does not mention that the patient had MI, NSTEMI, or STEMI. So the answer is No.',
    """
    Context: "CAD s/p NSTEMI as above"
    """.strip(),
    'Answer: The text mentions that the patient had NSTEMI. So the answer is Yes.',
]

example_C = [prompt + 
    """
    Context: "He was taken emergently to the cardiac catheterization lab."
    """.strip(),
    'Answer: The text does not mention that the patient had MI, NSTEMI, or STEMI. So the answer is No.',
    """
    Context: "PMH: ESRD as a result of DM on HD, DM related retinopathy/neuropathy; h/o infected tunneled catheter; hyperparathyroidism; HTN in the past; CAD s/p NSTEMI 12/74, echo in Jan 2074 showed EF 52%; CHF;  PVD with RLE ulcer followed by Dr."
    """.strip(),
    'Answer: The text mentions that the patient had NSTEMI. So the answer is Yes.',
    """
    Context: "Olivo is a 75-year-old right-handed woman with diabetes mellitus, HTN and dementia, and found with a ~ 11 cc R. BG/thalamic bleed with pan-ventricular extension with casted 3rd and 4th ventricles, and mild midline shift."
    """.strip(),
    'Answer: The text does not mention that the patient had MI, NSTEMI, or STEMI. So the answer is No.',
    """
    Context: "He was suffered NSTEMI in 11/72 in the setting of bactermia and Streptococcal cellulitis."
    """.strip(),
    'Answer: The text mentions that the patient had NSTEMI. So the answer is Yes.',
]

example_D = [prompt + 
    """
    Context: "Cardiac:  Regular rate and rhythm; no murmurs, rubs or gallops."
    """.strip(),
    "Answer: The text does not mention that the patient had MI, NSTEMI, or STEMI. So the answer is No.",
    """
    Context: "FH:  Mom had MI, age 50"
    """.strip(),
    "Answer: The text mentions that the patient's mother had MI at the age of 50, but it does not mention that the patient had MI, NSTEMI, or STEMI. So the answer is No.",
    """
    Context: "CAD s/p NSTEMI as above. Of note, in Oct-Nov 2111, had cardiac cath x 2.  Had NSTEMI on Oct 8, 2111    taken to cardiac cath    cath showed significant RCA disease and 40% prox LCx    c/b Vfib needing defib    stent placed for stenotic RCA lesion, c/b dissection needing 2nd stent placed."
    """.strip(),
    'Answer: The text mentions that the patient had NSTEMI. So the answer is Yes.',
    """
    Context: "ST elevation MI. which revealed an echo on 11/06/2074 with an EF of 25%, cardiac. The Cardiac Catheterization fellow was notified at 7:55."
    """.strip(),
    'Answer: The text mentions that the patient has a history of MI. So the answer is Yes.'
]

example_E = [prompt + 
    """
    Context: "Cardiac exam showed regular sinus rhythm, a normal S2 and no significant murmurs."
    """.strip(),
    "Answer: The text does not mention that the patient had MI, NSTEMI, or STEMI. So the answer is No.",
    """
    Context: "2/16/51 Pt had successful surgical repair of the pseudoaneurysm, complicated by a intraoperative NSTEMI with a peak troponin of .36."
    """.strip(),
    "Answer: The text mentions that the patient had NSTEMI. So the answer is Yes.",
    """
    Context: "His mother passed away from at 90 (no significant medical problems) and father at 66 from MI."
    """.strip(),
    'Answer: The text does not mention that the patient had MI, NSTEMI, or STEMI. So the answer is No.',
    """
    Context: "Assessment and plan   1. CAD: NSTEMI, on ASA, heparin, statin. 2b3a to start, cath pending in AM. Reason for visit   67 yo man with DM, supine HTN, orthostatic hypotension, hyperlipidemia, +FH presents with NSTEMI."
    """.strip(),
    'Answer: The text states that the patient had NSTEMI. So the answer is Yes.'
]

vicuna_13b_fine_tuned = ["These are some sentences from a patient's clinical report. Answer Yes or No to the final question. Does the text mention that the patient had MI, NSTEMI, STEMI, angina, pulmonary embolism, or pneumothorax? Let's think step by step.".strip()  + "\n\n" + """
    Context: "Cardiac etiology would be of greatest concern given hx of CAD and chest pain, though certainly cerebrovascular disease is present given CVA history."
    """.strip(),
    'Answer: The text does not mention that the patient had MI, NSTEMI, or STEMI. So the answer is No.',
    """
    Context: "Jain is a 67 year old male with a h/o DM, HTN, HL, Chronic Afib, PVD and bilateral popliteal aneurysm s/p R popliteal thrombosis w/ resultant RLE ischemia and dry gangrene of heel, toes and forefoot."
    """.strip(),
    'Answer: The text does not mention that the patient had MI, NSTEMI, or STEMI. So the answer is No.',
    """
    Context: "NSTEMI on Oct 8, 2111"
    """.strip(),
    'Answer: The text states that the patient had NSTEMI. So the answer is Yes.',
    """
    Context: "45 yo F w/ h/o DM, HTN, hypertriglyceridemia, tobacco use p/w SSCP and inferior STEMI."
    """.strip(),
    'Answer: The text states that the patient had STEMI. So the answer is Yes.',
    """
    Context: "His past medical history is significant for a coronary artery disease, status post IMI,afib,"
    """.strip(),
    'Answer: The text does not mention that the patient had MI, NSTEMI, or STEMI. So the answer is No.',
    """
    Context: "81 yo man with a history of DM2, HTN, CRI who presented with a NSTEMI and CHF."
    """.strip(),
    'Answer: The text states that the patient had NSTEMI. So the answer is Yes.',
    """
    Context: "Cardiac: Regular rate and rhythm."
    """.strip(),
    'Answer: The text does not mention that the patient had MI, NSTEMI, or STEMI. So the answer is No.'
]

example_dictionary = {
    "example_A": example_A,
    "example_B": example_B,
    "example_C": example_C,
    "example_D": example_D,
    "example_E": example_E,
    "vicuna_13b_fine_tuned": vicuna_13b_fine_tuned
}