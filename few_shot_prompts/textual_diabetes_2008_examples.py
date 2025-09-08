prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has diabetes? Answer Yes, No, Maybe, or Unmentioned to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "FAMILY HISTORY: Father with hypertension in his sixties , mother died of a vaginal cancer at a young age , daughter has asthma , and brother has hypertension."
    """.strip(),
    "Answer: The text does not mention if the patient has diabetes. So the answer is Unmentioned.",
    '''
    Context: "HISTORY OF PRESENT ILLNESS: This is a 56 year old with a history of insulin-dependent diabetes"
    '''.strip(),
    "Answer: The text mentions that the patient has diabetes. So the answer is Yes.",
    '''
    Context: "Her cardiac risk factors included hypercholesterolemia , hypertension , she was not diabetic , did not smoke , and had a plus or minus family history with a sister who died at 68 of a cardiac arrest."
    '''.strip(),
    "Answer: The text mentions that the patient does not have diabetes. So the answer is No.",
    '''
    Context: "*ENDO: questionable h/o DM"
    '''.strip(),
    "Answer: The text mentions that the patient has questionable history of diabetes. So the answer is Maybe.",
]

example_dictionary = {
    "example_A": example_A
}