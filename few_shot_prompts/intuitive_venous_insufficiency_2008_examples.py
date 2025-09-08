prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has venous insufficiency? Answer Yes, No, or Unsure to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "Jugular venous pressure approximately 8 centimeters."
    """.strip(),
    "Answer: The text does not mention that the patient has venous insufficiency. So the answer is No.",
    '''
    Context: "PAST MEDICAL HISTORY: The patient has a history of coronary artery disease and peripheral vascular disease."
    '''.strip(),
    "Answer: The text does not mention that the patient has venous insufficiency. So the answer is No.",
    '''
    Context: "This is a 60-year-old female with a history of chronic venous stasis ulcers of bilateral lower extremities admitted to the Plastic Includes chronic venous stasis ulcers in lower extremities ,"
    '''.strip(),
    "Answer: The text mentions that the patient has chronic venous stasis ulcers in both lower extremities. This is a condition often associated with venous insufficiency. So the answer is Yes.",
    '''
    Context: "Includes chronic venous stasis ulcers in lower extremities , diabetes mellitus , hypertension , asthma , sarcoid , restricted pulmonary disease , and obesity."
    '''.strip(),
    "Answer: The text mentions that the patient has chronic venous stasis ulcers in both lower extremities, which is a condition often associated with venous insufficiency. Additionally, the patient is being treated with medications such as labetalol, Norvasc, and Cozaar, which are commonly used to manage venous insufficiency and its associated conditions. So the answer is Yes.",
    '''
    Context: "PAST MEDICAL HISTORY: Diabetes , hypertension , hypercholesterolemia , chronic DVTs with pulmonary embolism x two , CVA , left temporal in the setting of an"
    '''.strip(),
    "Answer: The text does not mention that the patient has venous insufficiency. So the answer is No.",
    '''
    Context: "Neck showed no jugular venous distension."
    '''.strip(),
    "Answer: The text does not mention that the patient has venous insufficiency. So the answer is No." 
]

example_dictionary = {
    "example_A": example_A
}