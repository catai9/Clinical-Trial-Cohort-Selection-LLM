prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has asthma? Answer Yes, No, or Unsure to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "ALLERGY: NKA"
    """.strip(),
    "Answer: The text does not mention that the patient has asthma. So the answer is No.",
    '''
    Context: "Diverticulitis , CVA ( right cerebellar ) , colonic polyps , asthma , GERD ,"
    '''.strip(),
    "Answer: The text mentions that the patient has asthma. So the answer is Yes.",
    '''
    Context: "ALLERGIES:"
    '''.strip(),
    "Answer: The text does not mention that the patient has asthma. So the answer is No.",
    '''
    Context: "FAMILY HISTORY: Father with hypertension in his sixties , mother died of a vaginal cancer at a young age , daughter has asthma , and brother has hypertension. PAST MEDICAL HISTORY: Negative for asthma , tuberculosis , or HIV risk factors."
    '''.strip(),
    "Answer: The text mentions that the patient's daughter has asthma. The text mentions that the patient is negative for asthma. So the answer is No.",
    '''
    Context: "His blood pressure was 130/80 , pulse 55 , respiratory rate 12. He had no history of diabetes or previous hypertension."
    '''.strip(),
    "Answer: The text does not mention that the patient has asthma. So the answer is No.",
    '''
    Context: "ALLERGIES: Benadryl , which causes shortness of breath."
    '''.strip(),
    "Answer: The text does not mention that the patient has asthma. So the answer is No.",
]

example_dictionary = {
    "example_A": example_A
}