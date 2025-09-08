prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has depressive disorder (depression)? Answer Yes, No, Maybe, or Unmentioned to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "He did develop 1 millimeter of downsloping ST depressions in the lateral leads , and a pseudonormalization of the T-waves."
    """.strip(),
    "Answer: The text does not mention if the patient has depressive disorder (depression). So the answer is Unmentioned.",
    '''
    Context: "HISTORY OF PRESENT ILLNESS: This is a 37-year-old woman with a past medical history of depression , who is morbidly obese with a height of 5'3 and weight of 533 lb."
    '''.strip(),
    "Answer: The text mentions that the patient has depressive disorder (depression). So the answer is Yes.",
    '''
    Context: "BRIEF HISTORY OF PRESENT ILLNESS: Mr."
    '''.strip(),
    "Answer: The text does not mention if the patient has depressive disorder (depression). So the answer is Unmentioned.",
    '''
    Context: "He had two depressions infralaterally and was seen at CIMMC with question of restenosis."
    '''.strip(),
    "Answer: The text does not mention if the patient has depressive disorder (depression). So the answer is Unmentioned.",
    '''
    Context: "The patient was evaluated by the Psychiatry Service for some features of hypomania on 17 of May"
    '''.strip(),
    "Answer: The text does not mention if the patient has depressive disorder (depression). So the answer is Unmentioned.",
    '''
    Context: "He was also started on Zoloft on postop day 2 at 75 mg p.o. daily for his anxiety."
    '''.strip(),
    "Answer: The text does not mention if the patient has depressive disorder (depression). So the answer is Unmentioned.",
    '''
    Context: "Pt also started on empiric qhs acetazolamide per pulmonary recs based on recent data showing that it improves symptoms in pt's with central sleep apnea and heart failure."
    '''.strip(),
    "Answer: The text does not mention if the patient has depressive disorder (depression). So the answer is Unmentioned.",
]

example_dictionary = {
    "example_A": example_A
}