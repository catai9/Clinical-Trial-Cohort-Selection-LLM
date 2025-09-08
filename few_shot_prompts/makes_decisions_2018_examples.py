prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient does not make their own decision? Answer Yes or No to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "Xie send a paring for fungal culture before we consider it."
    """.strip(),
    "Answer: The text makes no mention of the patient's decision making abilities or other factors. So the answer is No.",
    '''
    Context: "In PVH ED, pt describes the pain as like a bleeding scar and states my heart is bloated through her daughter who acted as her interpreter.
    '''.strip(),
    "Answer: The text makes no mention of the patient's decision making abilities or other factors. So the answer is No.",
    '''
    Context: "The patient's daughter makes decisions for the patient."
    '''.strip(),
    "Answer: The text mentions that the patient's daughter makes decisions for the patient. This means that the patient does not make their own decision. So the answer is Yes.",
    '''
    Context: "The patient has dementia."
    '''.strip(),
    "Answer: The text mentions that the patient has dementia. This means that the patient does not make their own decision. So the answer is Yes.",
    '''
    Context: Source: Chart and Pt.'s husband - Pt is non-verbal.
    '''.strip(),
    "Answer: The text mentions that the patient is non-verbal, but it does not explicitly state that the patient cannot make their own decisions or has a caretaker. So the answer is No.",
    '''
    Context: her husband, who is the primary care giver
    '''.strip(),
    "Answer: The text mentions that the patient's husband is their primary caretaker. Primary caretakers make decisions for the patient. So the answer is Yes."
]

example_B = [prompt + 
    """
    Context: "SOCIAL Hx: The Pt lives at home w/ his wife (49yo in good health) and son (27yo in good health)."
    """.strip(),
    "Answer: The text makes no mention of the patient's decision making abilities or other factors. So the answer is No.",
    '''
    Context: "I had the pleasure of participating in the care of VivianLee Jorgenson during her recent hospitalization at Goulds Hospital."
    '''.strip(),
    "Answer: The text makes no mention of the patient's decision making abilities or other factors. So the answer is No.",
    '''
    Context: "SH: Lives with husband, who sounds like he is primary caregiver."
    '''.strip(),
    "Answer: The text mentions that the patient's husband is their primary caretaker. Primary caretakers make decisions for the patient. So the answer is Yes.",
    '''
    Context: "I suspect she has been under someone else's care since I never prescribed Glyburide, Actos and Insulin."
    '''.strip(),
    "Answer: The text mentions that the patient has been under someone else's care but makes no mention of the patient's decision making abilities or other factors. So the answer is No.",
    '''
    Context: "SH:lives with daughter (Grace) who provides FT care; unable to perform ADL/IADLs."
    '''.strip(),
    "Answer: The text mentions that the patient's daughter provides the patient with FT care. So the answer is Yes.",
    '''
    Context: "The patient was seen by his primary care physician,"
    '''.strip(),
    "Answer: The text makes no mention of the patient's decision making abilities or other factors. So the answer is No."
]

example_C = [prompt + 
    """
    Context: "Willow Gardens Care Center   left main severe; left anterior descending 70%; CX ostial disease; right coronary artery moderate to severe; PLV .80 to .90"
    """.strip(),
    "Answer: The text makes no mention of the patient's decision making abilities or other factors. So the answer is No.",
    '''
    Context: "Daily wound care per the following protocol; 1.  Normal saline irrigation 30 cc x 3.  A thin layer of 50% Diprolene ointment 0.05% with Bactroban cream to the wound bed and the wide periwound margin."
    '''.strip(),
    "Answer: The text makes no mention of the patient's decision making abilities or other factors. So the answer is No.",
    '''
    Context: "Daughter, Yolanda, is the HCP (817-638-1328) and primary caregiver."
    '''.strip(),
    "Answer: The text mentions that the patient's daughter is their primary caretaker. Primary caretakers make decisions for the patient. So the answer is Yes.",
    '''
    Context: "It was our pleasure to care for Mr. Johnson Family Vision Care, It has been my great pleasure to participate in his care."
    '''.strip(),
    "Answer: The text makes no mention of the patient's decision making abilities or other factors. So the answer is No.",
    '''
    Context: "SOCIAL HISTORY: Lives with wife who is primary caretaker."
    '''.strip(),
    "Answer: The text mentions that the patient's wife is their primary caretaker. Primary caretakers make decisions for the patient. So the answer is Yes.",
    '''
    Context: "He is seeking to establish a new relationship with a primary care physician through Barney Convalescent Hospital."
    '''.strip(),
    "Answer: The text makes no mention of the patient's decision making abilities or other factors. So the answer is No."
]

example_D = [prompt + 
    """
    Context: "FAMILY HISTORY:  Reveals her mother passed away at age 73 with malignancy, father passed away at age 89 with congestive heart failure with five bypasses, sister at age 73 with arthritis, a brother at age 70 with colon cancer and MI, sister age 68 has diabetes and Alzheimers, brother 63 years old in good health."
    """.strip(),
    "Answer: The text makes no mention of the patient's decision making abilities or other factors. So the answer is No.",
    """
    Context: "She represents to the ED today after her husband, who is the primary care giver noted on the morning of admit that the catheter was not draining, but the pt. was incont."
    """.strip(),
    "Answer: The text mentions that the patient's husband is their primary caregiver and that a VNA (Visiting Nurse Association) has come into the patient's home to help with care. So the answer is Yes.",
    """
    Context: "He is married with two sons, age 21 and 18, both of whom are in good health. We have encouraged him to call with any questions, concerns or changes in health status."
    """.strip(),
    'Answer: The text mentions that the patient is married and has two sons, but makes no mention of the patient\'s decision making abilities or other factors. So the answer is No.',
    """
    Context: "The patient lives with his wife and son and is a retired Fire Chief."
    """.strip(),
    'Answer: The text mentions that the patient lives with his wife and son, but makes no mention of the patient\'s decision making abilities or other factors. So the answer is No.',
    """
    Context: "SOCIAL HISTORY: Lives with wife who is primary caretaker."
    """.strip(),
    'Answer: The text mentions that the patient\'s wife is their primary caretaker. Primary caretakers make decisions for the patient. So the answer is Yes.',
    """
    Context: "SH:lives with daughter (Grace) who provides FT care; unable to perform ADL/IADLs."
    """.strip(),
    "Answer: The text mentions that the patient's daughter provides the patient with FT care. So the answer is Yes."
]

example_E = [prompt + 
    """
    Context: "He was in his usual state of health when he woke up at 8 am."
    """.strip(),
    "Answer: The text makes no mention of the patient's decision making abilities or other factors. So the answer is No.",
    """
    Context: "rehab, and we will defer that decision to him. currently 60 but was in her usual state of good health until 2065 when she"
    """.strip(),
    "Answer: The text makes no mention of the patient's decision making abilities or other factors. So the answer is No.",
    """
    Context: "SOCIAL HISTORY: Lives with wife who is primary caretaker."
    """.strip(),
    'Answer: The text mentions that the patient\'s wife is their primary caretaker. Primary caretakers make decisions for the patient. So the answer is Yes.',
    """
    Context: "Because pt was not having any symptoms of angina, the decision was made not to intervene on the LCX lesion and to stress the pt at a later date."
    """.strip(),
    'Answer: The text makes no mention of the patient\'s decision making abilities or other factors. So the answer is No.',
    """
    Context: "Comes to review her medical problems."
    """.strip(),
    'Answer: The text makes no mention of the patient\'s decision making abilities or other factors. So the answer is No.',
    """
    Context: "Daughter, Yolanda, is the HCP (817-638-1328) and primary caregiver."
    """.strip(),
    'Answer: The text mentions that the patient\'s daughter is the HCP and primary caregiver. So the answer is Yes.'
]

vicuna_13b_fine_tuned = ["""
These are some sentences from a patient's clinical report. Does the patient make their own decision? Answer No, only if it is explicitly stated that the patient has dementia, mental retardation, or has a caretaker. Let's think step by step.

    Context: "Xie send a paring for fungal culture before we consider it."
    """.strip(),
    "Answer: The text makes no mention of the patient's decision making abilities or other factors. So the answer is Yes.",
    '''
    Context: "In PVH ED, pt describes the pain as like a bleeding scar and states my heart is bloated through her daughter who acted as her interpreter.
    '''.strip(),
    "Answer: The text makes no mention of the patient's decision making abilities or other factors. So the answer is Yes.",
    '''
    Context: "The patient's daughter makes decisions for the patient."
    '''.strip(),
    "Answer: The text mentions that the patient's daughter makes decisions for the patient. So the answer is No.",
    '''
    Context: "The patient has dementia."
    '''.strip(),
    "Answer: The text mentions that the patient has dementia. So the answer is No.",
    '''
    Context: Source: Chart and Pt.'s husband - Pt is non-verbal.
    '''.strip(),
    "Answer: The text mentions that the patient is non-verbal, but it does not explicitly state that the patient cannot make their own decisions or has a caretaker. So the answer is Yes.",
    '''
    Context: her husband, who is the primary care giver
    '''.strip(),
    "Answer: The text mentions that the patient's husband is their primary caretaker. So the answer is No.",
    '''
    Context: Daughter, Yolanda, is the HCP (817-638-1328) and primary caregiver
    '''.strip(),
    "Answer: The text mentions that the patient's daughter is their primary caretaker. So the answer is No.",
    '''
    Context: Patient is a single parent to a 15-year-old son and a 10-year-old daughter
    '''.strip(),
    "Answer: The text mentions that the patient takes care of a son and daughter but does not mention that they are the patient's caretaker. So the answer is Yes.",
    '''
    Context: It was so bad that he was unable to feed himself, and needed help from his wife to do so.
    '''.strip(),
    "Answer: The text mentions that his wife helps feed him but does not state that she is his caretaker. So the answer is Yes.",
    '''
    Context: patient's daughter reports that she bought him new long underwear
    '''.strip(),
    "Answer: The text does not state that the patient's daughter is their caregiver. So the answer is Yes.",
    '''
    Context: In PVH ED, pt describes the pain as like a bleeding scar and states my heart is bloated through her daughter who acted as her interpreter.
    '''.strip(),
    "Answer: The text mentions that her daughter is her interpreter but does not state that her daughter is her caregiver. So the answer is Yes.",
    '''
    Context: Daughter in with her. Three daughters and 2 sons are very involved with her.
    '''.strip(),
    "Answer: The text mentions that her children are involved with her but do not state that the patient has a caretaker. So the answer is Yes.",
    '''
    Context: The patient lives with her husband who helps her with ADLs because she is hemiparetic
    '''.strip(),
    "Answer: The text mentions that her husband helps her but does not state that he acts as her caretaker. So the answer is Yes.",
    '''
    Context: She spends a lot of time caring for her partially disabled husband.
    '''.strip(),
    "Answer: The text does not mention that she is his caretaker or he cannot make his own decisions. So the answer is Yes."
]

example_dictionary = {
    "example_A": example_A,
    "example_B": example_B,
    "example_C": example_C,
    "example_D": example_D,
    "example_E": example_E,
    "vicuna_13b_fine_tuned": vicuna_13b_fine_tuned
}