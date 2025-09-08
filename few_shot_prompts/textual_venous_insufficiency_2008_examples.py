prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has venous insufficiency? Answer Yes, No, Maybe, or Unmentioned to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "On exam , patient was noted to have positive jugular venous distension , 3/6 systolic murmur at the left upper sternal border , right lower quadrant tenderness to palpation , abdomen soft and without rebound tenderness."
    """.strip(),
    "Answer: The text does not mention if the patient has venous insufficiency. So the answer is Unmentioned.",
    '''
    Context: "This is an 87-year-old female with a history of congestive heart failure , atrial fibrillation status post pacemaker placement , and chronic venous stasis who presents with nausea , vomiting , and failure to thrive"
    '''.strip(),
    "Answer: The text mentions that the patient has chronic venous stasis. Chronic venous stasis is another term for venous insufficiency. So the answer is Yes.",
    '''
    Context: "There is no jugular venous distention , no lymphadenopathy."
    '''.strip(),
    "Answer: The text does not mention if the patient has venous insufficiency. So the answer is Unmentioned.",
    '''
    Context: "Reports increasing SOB over last several months , increased leg edema with 10 lb weight gain."
    '''.strip(),
    "Answer: The text does not mention if the patient has venous insufficiency. So the answer is Unmentioned.",
    '''
    Context: "On exam , patient was noted to have positive jugular venous distension , 3/6 systolic murmur at the left upper sternal border , right lower quadrant tenderness to palpation , abdomen soft and without rebound tenderness."
    '''.strip(),
    "Answer: The text does not mention if the patient has venous insufficiency. So the answer is Unmentioned.",
    '''
    Context: "PRINCIPAL DISCHARGE DIAGNOSIS ;Responsible After Study for Causing Admission ) flash pulmonary edema"
    '''.strip(),
    "Answer: The text does not mention if the patient has venous insufficiency. So the answer is Unmentioned.",
    '''
    Context: "Pulm: bibasilar crakles R>L , distant breath sounds Abdomen: large pannus , RUQ scar from prior appy , soft , NT , ND , BS+. Ext: No edema , +brawny venous stasis feet b/l , palpable thrill on pt's right distal forearm at site of pt's a-v fistula."
    '''.strip(),
    "Answer: The text does not mention if the patient has venous insufficiency. So the answer is Unmentioned.",
    '''
    Context: "Severe Left Carotid Stenosis LEFT CAROTID ENDTARTERECTOMY WITH PATCH ANGIOPLASTY"
    '''.strip(),
    "Answer: The text does not mention if the patient has venous insufficiency. So the answer is Unmentioned.",
    '''
    Context: "PAST MEDICAL HISTORY: Diabetes , hypertension , hypercholesterolemia , chronic DVTs with pulmonary embolism x two , CVA , left temporal in the setting of a"
    '''.strip(),
    "Answer: The text does not mention if the patient has venous insufficiency. So the answer is Unmentioned.",
]

example_dictionary = {
    "example_A": example_A
}