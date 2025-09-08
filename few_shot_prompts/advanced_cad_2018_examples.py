prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has advanced cardiovascular disease (CAD). "Advanced" is defined as having two or more of the following: Taking 2 or more medications to treat CAD, History of myocardial infarction (MI), Currently experiencing angina, and Ischemia, past or present. Answer Yes or No to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "PRESENTING COMPLAINT:  The patient is a 48-year-old female who has had a kidney transplant as well as an extensive cardiac history who comes in complaining of fatigue and shortness of breath."
    """.strip(),
    'Answer: The text does not mention that the patient has advanced cardiovascular disease (CAD) and the text does not mention that the patient has two or more of the aforementioned symptoms. So the answer is No.',
    """
    Context: "The myocardial scans are within normal limits and do not demonstrate evidence of myocardial ischemia or infarction. The ECG response to pharmacological stress was  negative for ischemia. Cardiovascular:  no history of hypertension, no MI; hx of well controlled angina, uses NTG rarely, very little exercise, no ankle edema, syncope."
    """.strip(),
    'Answer: The text does not mention that the patient has advanced cardiovascular disease (CAD) and the text does not mention that the patient has two or more of the aforementioned symptoms. So the answer is No.',
    """
    Context: "FAMILY HISTORY:  Positive for coronary artery disease, breast cancer and diabetes."
    """.strip(),
    'Answer: The text mentions that the patient has coronary artery disease but the text does not mention another of the aforementioned symptoms. "Advanced" is defined as having two or more of the aforementioned symptoms. However, only one of the symptoms is mentioned. So the answer is No.',
    """
    Context: "1.  Angina pectoris. cardiovascular exam showed a regular rate and rhythm. manifested by myocardial infarction approximately five years ago. CARDIOVASCULAR:  His Since MI, has been doing well on atenolol, asa, lasix, lisinopril, and amlidopine.
    """.strip(),
    'Answer: The text mentions that the patient is taking 2 or more medications to treat CAD and has a history of myocardial infarction (MI). "Advanced" is defined as having two or more of the aforementioned symptoms. The text mentions two of the listed symptoms. So the answer is Yes.'
]

example_B = [prompt + 
    """
    Context: "His mother passed away from at 90 (no significant medical problems) and father at 66 from MI."
    """.strip(),
    'Answer: The text does not mention that the patient has advanced cardiovascular disease (CAD) and the text does not mention that the patient has two or more of the aforementioned symptoms. So the answer is No.',
    """
    Context: "CV Ischemia: S/p NSTEMI Cardiovascular: no CP as above Cardiovascular Ischemia:  Has CRI, and just had a NSTEMI with a Troponin peak at 2.91 on 3/23, but now with an increase to 3.73."
    """.strip(),
    'Answer: The text mentions that the patient has a history of NSTEMI which is a type of myocardial infarction (MI) and the patient has ischemia. "Advanced" is defined as having two or more of the aforementioned symptoms. The text mentions two of the listed symptoms. So the answer is Yes.',
    """
    Context: "He has an elevated wbc and an increased creatinine to 1.6; his chest x-ray is consistent with a RUL and RML pneumonia, and he has a low bnp negative for cardiac stretching."
    """.strip(),
    'Answer: The text does not mention that the patient has advanced cardiovascular disease (CAD) and the text does not mention that the patient has two or more of the aforementioned symptoms. So the answer is No.',
    """
    Context: "In this setting, a dobutamine stress test performed last June showed no evidence of provokable ischemia. Olivier has evidence of continuing chest and left shoulder discomfort which she believes is similar to her pre-bypass surgery angina. She had recurrence of her typical angina at home, took three nitroglycerin with minimal relief, and activated the 911 system. This is 
    comparable to a previous electrocardiogram in October, which may have been her most recent presentation with ischemia. Currently it is not clear to me that her symptoms are secondary to recurrent ischemia,
    however I will have her undergo an exercise tolerance test (adenosine MIBI) to help to further evaluate this.
    """.strip(),
    'Answer: The text mentions that the patient has ischemia and angina. "Advanced" is defined as having two or more of the aforementioned symptoms. The text mentions two of the listed symptoms. So the answer is Yes.'
]

example_C = [prompt + 
    """
    Context: "The ECG response to pharmacological stress was  negative for ischemia."
    """.strip(),
    'Answer: The text does not mention that the patient has advanced cardiovascular disease (CAD) and the text does not mention that the patient has two or more of the aforementioned symptoms. So the answer is No.',
    """
    Context: "Focused problem list:  Hypotension limiting hemodialysis s/p MI 3 months ago, DM, neuropathy, depression. Since then she has had bouts of what appears to be her anginal equivalent- left ear pain and a sense of fullness in her lower chest that occur at rest and are fleeting, going away before she has time to try a SLTNG."
    """.strip(),
    'Answer: The text mentions that the patient has a history of non-ST elevation MI and angina. "Advanced" is defined as having two or more of the aforementioned symptoms. The text mentions two of the listed symptoms. So the answer is Yes.',
    """
    Context: "2. Chest pain with bigeminy and PVCs:  Rule out for MI by enzymes x3, as ?new dysrhythmia may signify ?myocardial irritation/damage."
    """.strip(),
    'Answer: The text does not mention that the patient has advanced cardiovascular disease (CAD) and the text does not mention that the patient has two or more of the aforementioned symptoms. So the answer is No.',
    """
    Context: "-Ischemia- angina resolved with nitrates, reviewed EKG with Dr."
    """.strip(),
    'Answer: The text mentions that the patient has ischemia and angina. "Advanced" is defined as having two or more of the aforementioned symptoms. The text mentions two of the listed symptoms. So the answer is Yes.'
]

example_D = [prompt + 
    """
    Context: "The Pt may have had an exertional ischemia but the lack of CP and EKGs changes makes this less likely; however, the Pt has been asymptomatic on the floor and so no EKG tracings concomitant with the SOB are available to completely rule out this possibility. HPI: This is a 73yo male w/ a complicated PMH that includes HTN, DM, hyperlipidemia, CAD, and a past MI, which resulted in the placement of an AICD, who now p/w severe SOB and DOE."
    """.strip(),
    'Answer: The text mentions that the patient has a history of myocardial infarction (MI) and is currently experiencing ischemia. "Advanced" is defined as having two or more of the aforementioned symptoms. The text mentions two of the listed symptoms. So the answer is Yes.',
    """
    Context: "HISTORY OF PRESENT ILLNESS:  This is an elderly patient, 82, with known diabetes and coronary artery disease, which has required placement of a pacemaker."
    """.strip(),
    'Answer: The text does not mention that the patient has advanced cardiovascular disease (CAD) and the text does not mention that the patient has two or more of the aforementioned symptoms. So the answer is No.',
    """
    Context: "The scan results demonstrated no evidence of ischemia and/or scar."
    """.strip(),
    'Answer: The text does not mention that the patient has advanced cardiovascular disease (CAD) and the text does not mention that the patient has two or more of the aforementioned symptoms. So the answer is No.',
    """
    Context: "The differential for chest pain is broad and includes cardiac ischemia, myocardial infarction, aortic dissection, pneumothorax, pulmonary embolus, bronchitis, pleurisy, GERD/esophageal spasm, musculoskeletal/chest wall pain, and anxiety."
    """.strip(),
    'Answer: The text mentions that the patient has a history of myocardial infarction (MI) and is currently experiencing ischemia. "Advanced" is defined as having two or more of the aforementioned symptoms. The text mentions two of the listed symptoms. So the answer is Yes.'
]

example_E = [prompt + 
    """
    Context: "Cardiovascular: No MI, CHF, rheumatic heart disease. -H/o Transient ischemic attack 2073"
    """.strip(),
    'Answer: The text does not mention that the patient has advanced cardiovascular disease (CAD). The text mentions ischemia, but the text does not mention that the patient has two or more of the aforementioned symptoms. So the answer is No.',
    """
    Context: "angina status post MI, remained hemodynamically stable, and is; DIAGNOSIS:  Chest pain, rule out unstable angina."
    """.strip(),
    'Answer: The text mentions that the patient has a history of non-ST segment elevation myocardial infarction (NSTEMI) and angina. "Advanced" is defined as having two or more of the aforementioned symptoms. The text mentions two of the listed symptoms. So the answer is Yes.',
    """
    Context: "He denies angina, congestive heart failure, or arrhythmias. It is also possible that this is related to angina. 3.  Other related risks. Mother unknown, father had onset of angina in his 80s."
    """.strip(),
    'Answer: The text does not mention that the patient has advanced cardiovascular disease (CAD) and the text does not mention that the patient has two or more of the aforementioned symptoms. So the answer is No.',
    """
    Context: "c. Ischemia - was stented x 2 to the prox RCA lesion and was on integrilin x 24hrs prior. also, of note on cardiovascular examination, has a soft murmur with EKG changes, he will also be admitted for rule out MI. His complaint of some mild chest pain (not same as anginal pain day before) thought to be from defibrillation."
    """.strip(),
    'Answer: The text mentions that the patient has a history of ischemia and recently experienced angina. "Advanced" is defined as having two or more of the aforementioned symptoms. The text mentions two of the listed symptoms. So the answer is Yes.'
]

vicuna_13b_fine_tuned = ["""
These are some sentences from a patient's clinical report. Answer Yes or No to the final question.

{}

Question: Does the text mention that the patient has advanced cardiovascular disease (CAD). "Advanced" is defined as having two or more of the following: 
- Taking 2 or more medications to treat CAD
- History of myocardial infarction(MI)
- Currently experiencing angina
- Ischemia, past or present
"""
]

example_dictionary = {
    "example_A": example_A,
    "example_B": example_B,
    "example_C": example_C,
    "example_D": example_D,
    "example_E": example_E,
    "vicuna_13b_fine_tuned": vicuna_13b_fine_tuned
}