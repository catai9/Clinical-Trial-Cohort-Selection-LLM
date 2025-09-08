prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has serum creatinine more than 1.5 mg/dl? Answer Yes or No to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "HGB A1c is 7.0, Hct is down to 31.6, epo 37, creatinine stable at 1.6, MCV 93.3.  Most likely anemia of chronic illness but need to check smear and stools"
    """.strip(),
    'Answer: The text mentions that the patient has a serum creatinine level of 1.6. 1.6 is more than 1.5 mg/dl. So the answer is Yes.',
    """
    Context: "Plasma Creatinine                1.34                      (0.60-1.50)    mg/dl"
    """.strip(),
    'Answer: The text mentions that the patient has a serum creatinine level of 1.34. 1.34 is less than 1.5 mg/dl. So the answer is No.',
    """
    Context: "Direct Bilirubin                 0.1                       (0-0.4)        mg/dl"
    """.strip(),
    'Answer: The text does not mention the serum creatinine level of the patient. So the answer is No.',
    """
    Context: "bicarbonate 29, BUN 36, creatinine 3.5, glucose 263, CK 281,"
    """.strip(),
    'Answer: The text mentions that the patient has a serum creatinine level of 3.5. 3.5 is more than 1.5 mg/dl. So the answer is Yes.'
]

example_B = [prompt + 
    """
    Context: "Creatinine     3.4"
    """.strip(),
    'Answer: The text mentions that the patient has a serum creatinine level of 3.4. 3.4 is more than 1.5 mg/dl. So the answer is Yes.',
    """
    Context: "CREATININE                       1.7              H        (0.6-1.3)      MG/DL"
    """.strip(),
    'Answer: The text mentions that the patient has a serum creatinine level of 1.7. 1.7 is more than 1.5 mg/dl. So the answer is Yes.',
    """
    Context: "Renal/Genitourinary: no history of renal failure; denies hematuria, dysuria, obstructive uropathy"
    """.strip(),
    'Answer: The text does not mention the serum creatinine level of the patient. So the answer is No.',
    """
    Context: "Plasma Creatinine                0.9"
    """.strip(),
    'Answer: The text mentions that the patient has a serum creatinine level of 0.9. 0.9 is less than 1.5 mg/dl. So the answer is No.'
]

example_C = [prompt + 
    """
    Context: "Preop Creatinine: 1.64"
    """.strip(),
    'Answer: The text mentions that the patient has a serum creatinine level of 1.64. 1.64 is more than 1.5 mg/dl. So the answer is Yes.',
    """
    Context: "Creatinine (Stat Lab)    0.6                         (0.6-1.5)        mg/dl"
    """.strip(),
    'Answer: The text mentions that the patient has a serum creatinine level of 0.6. 0.6 is less than 1.5 mg/dl. So the answer is No.',
    """
    Context: "Laboratory Data:  His hematocrit was 39.9.  Platelets were within normal limits."
    """.strip(),
    'Answer: The text does not mention the serum creatinine level of the patient. So the answer is No.',
    """
    Context: "Microalbumin 12/14/2115 6.5"
    """.strip(),
    'Answer: The text does not mention the serum creatinine level of the patient. So the answer is No.'
]

example_D = [prompt + 
    """
    Context: "We have reviewed pre procedural expectations and procedural risk including femoral vascular complications, cardiac perforation, renal complications, stroke, heart attack, and death."
    """.strip(),
    "Answer: The text does not mention the serum creatinine level of the patient. So the answer is No.",
    """
    Context: "Plasma Creatinine                0.9"
    """.strip(),
    "Answer: The text mentions that the patient has a serum creatinine level of 0.9. 0.9 is less than 1.5 mg/dl. So the answer is No.",
    """
    Context: "Creatinine (Stat Lab)            4.2              H        (0.6-1.5)        mg/dl"
    """.strip(),
    'Answer: The text mentions that the patient has a serum creatinine level of 4.2. 4.2 is more than 1.5 mg/dl. So the answer is Yes.',
    """
    Context: "bicarbonate 29, BUN 36, creatinine 3.5, glucose 263, CK 281,"
    """.strip(),
    'Answer: The text mentions that the patient has a serum creatinine level of 3.5. 3.5 is more than 1.5 mg/dl. So the answer is Yes.'
]

example_E = [prompt + 
    """
    Context: "He is on lisinopril 1.25 mg and has had great difficulty tolerating any higher dose due to dizziness."
    """.strip(),
    "Answer: The text does not mention the serum creatinine level of the patient. So the answer is No.",
    """
    Context: "4. Renal insufficiency, creatinine 1.6."
    """.strip(),
    "Answer: The text mentions that the patient has a serum creatinine level of 1.6. 1.6 is more than 1.5 mg/dl. So the answer is Yes.",
    """
    Context: "Creatinine 3.4; glucose 136."
    """.strip(),
    'Answer: The text mentions that the patient has a serum creatinine level of 3.4. 3.4 is more than 1.5 mg/dl. So the answer is Yes.',
    """
    Context: "Plasma Creatinine                1.17                      (0.60-1.50)    mg/dl"
    """.strip(),
    'Answer: The text mentions that the patient has a serum creatinine level of 1.17. 1.17 is less than 1.5 mg/dl. So the answer is No.'
]

vicuna_13b_fine_tuned = ["These are some sentences from a patient's clinical report. Answer only a single value. What is the patient's creatinine level?".strip()  + "\n\n" +   """
    Context: "HGB A1c is 7.0, Hct is down to 31.6, epo 37, creatinine stable at 1.6, MCV 93.3.  Most likely anemia of chronic illness but need to check smear and stools"
    """.strip(),
    '1.6',
    """
    Context: "Plasma Creatinine                1.34                      (0.60-1.50)    mg/dl"
    """.strip(),
    '1.34',
    """
    Context: "Direct Bilirubin                 0.1                       (0-0.4)        mg/dl"
    """.strip(),
    'Unsure',
    """
    Context: "HEMOGLOBIN A1C, WB               6.1                       (3.9-6.1)      %"
    """.strip(),
    'Unsure',
    """
    Context: "Plasma Creatinine                0.9"
    """.strip(),
    '0.9',

    """
    Context: "bicarbonate 29, BUN 36, creatinine 3.5, glucose 263, CK 281,"
    """.strip(),
    '3.5',                
    """
    Context: "(baseline creatinine 2), vascular risk factors as delineated and"
    """.strip(),
    '2',
    """
    Context: "baseline creatinine 1.8-2.2"
    """.strip(),
    '1.8'
]

example_dictionary = {
    "example_A": example_A,
    "example_B": example_B,
    "example_C": example_C,
    "example_D": example_D,
    "example_E": example_E,
    "vicuna_13b_fine_tuned": vicuna_13b_fine_tuned
}