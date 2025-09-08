prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has a hemoglobin value below 6.5% or above 9.5%? Answer Yes or No to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "HGB A1c is 7.0, Hct is down to 31.6, epo 37, creatinine stable at 1.6, MCV 93.3.  Most likely anemia of chronic illness but need to check smear and stools"
    """.strip(),
    'Answer: The text mentions that the patient has a hemoglobin value of 7.0. 7.0 is above 6.5 and less than 9.5. So the answer is No.',
    """
    Context: "Diabetes:  Had been on glyburide, currently diet controlled, 11/25 A1c 6.3"
    """.strip(),
    'Answer: The text mentions that the patient has a hemoglobin value of 6.3. 6.3 is below 6.5. So the answer is Yes.',
    """
    Context: "was thought to be anemic with a hematocrit of 25 on evaluation at "
    """.strip(),
    'Answer: The text does not mention the hemoglobin value of the patient. So the answer is No.',
    """
    Context: "LABORATORY EVALUATION:  CBC:  White count 8.9, hematocrit 40.8, "
    """.strip(),
    'Answer: The text does not mention the hemoglobin value of the patient. So the answer is No.'
]

example_B = [prompt + 
    """
    Context: "Last HgbA1c was in October and was 7.7 which is a moderate improvement for him."
    """.strip(),
    'Answer: The text mentions that the patient has a hemoglobin value of 7.7. 7.7 is above 6.5 and less than 9.5. So the answer is No.',
    """
    Context: " HGB                              13.5                      (12.0-16.0)      gm/dl"
    """.strip(),
    'Answer: The text mentions that the patient has a hemoglobin value of 13.5. 13.5 is above 9.5. So the answer is Yes.',
    """
    Context: "1. Diabetes: good A1c in Nov. 10. "
    """.strip(),
    'Answer: The text does not mention the hemoglobin value of the patient. So the answer is No.',
    """
    Context: "- DM2 - no known microvascular disease; last A1c 7.3 (June 36)"
    """.strip(),
    'Answer: The text mentions that the patient has a hemoglobin value of 7.3. 7.3 is above 6.5 and less than 9.5. So the answer is No.'
]

example_C = [prompt + 
    """
    Context: "HGB                     10.9      L              12.0-16.0      gm/dl"
    """.strip(),
    'Answer: The text mentions that the patient has a hemoglobin value of 10.9. 10.9 is above 9.5. So the answer is Yes.',
    """
    Context: "Her A1c today was 6.6, which represents excellent control despite a fairly high glucoses she was recording."
    """.strip(),
    'Answer: The text mentions that the patient has a hemoglobin value of 6.6. 6.6 is above 6.5 and less than 9.5. So the answer is No.',
    """
    Context: "METFORMIN 1000 MG (1000MG TABLET take 1) PO BID"
    """.strip(),
    'Answer: The text does not mention the hemoglobin value of the patient. So the answer is Yes.',
    """
    Context: "hgba1c 6.5 (decreased from 8.9 in 11/77) creatinine stable at 1.4"
    """.strip(),
    'Answer: The text mentions that the patient has a hemoglobin value of 6.5. 6.5 is not below 6.5. So the answer is No.'
]

example_D = [prompt + 
    """
    Context: "HGB                              13.5                      (12.0-16.0)      gm/dl"
    """.strip(),
    "Answer: The text mentions that the patient has a hemoglobin value of 13.5. 13.5 is above 9.5. So the answer is Yes.",
    """
    Context: "- DM2 - no known microvascular disease; last A1c 7.3 (June 36)"
    """.strip(),
    "Answer: The text mentions that the patient has a hemoglobin value of 7.3. 7.3 is above 6.5 and less than 9.5. So the answer is No.",
    """
    Context: "Heme/Onc:  no history of bleeding, blood diseases; no history of malignancy, chemotherapy, or radiation therapy"
    """.strip(),
    'Answer: The text does not mention the hemoglobin value of the patient. So the answer is Yes.',
    """
    Context: "    Date     GLOB     HGB      MCV      MCH      MCHC     RDW      UA-KET   UA-WBC  \n01/20/79 3.6      16.8     89       30.4     34.3     12.9     NEGATIVE NEGATIVE"
    """.strip(),
    'Answer: The text mentions that the patient has a hemoglobin value of 16.8. 16.8 is above 9.5. So the answer is Yes.'
]

example_E = [prompt + 
    """
    Context: "He continues to take insulin and his last hemoglobin A1c was 6.6.  He has had two recent episodes of mild hypoglycemia."
    """.strip(),
    "Answer: The text mentions that the patient has a hemoglobin value of 6.6. 6.6 is above 6.5 and less than 9.5. So the answer is No.",
    """
    Context: "Labs: HbAIC 8.10% 8/76\nHowever, he had a normal fasting sugar of 104 and a hemoglobin A1C of 6.20."
    """.strip(),
    "Answer: The text mentions that the patient has a hemoglobin value of 8.10. 8.10 is above 6.5 and less than 9.5. So the answer is No.",
    """
    Context: "1/17/73: hgb A1c 6.80, mean glucose 141"
    """.strip(),
    'Answer: The text mentions that the patient has a hemoglobin value of 6.5 and 6.8. Both values are above 6.5 and less than 9.5. So the answer is No.',
    """
    Context: "Hemoglobin A1C       10.20H  3.80-6.40 %        12/12/11 10:34   10.20(H) "
    """.strip(),
    'Answer: The text mentions that the patient has a hemoglobin value of 10.20%. 10.20% is above 9.5%. So the answer is Yes.'
]

vicuna_13b_fine_tuned = ["These are some sentences from a patient's clinical report. Answer only a single value. What is the patient's most recent hemoglobin A1c (HbA1c) value?".strip()  + "\n\n" + """
    Context: "HGB A1c is 7.0, Hct is down to 31.6, epo 37, creatinine stable at 1.6, MCV 93.3.  Most likely anemia of chronic illness but need to check smear and stools"
    """.strip(),
    '7.0',
    """
    Context: "Diabetes:  Had been on glyburide, currently diet controlled, 11/25 A1c 6.3"
    """.strip(),
    '6.3',
    """
    Context: "was thought to be anemic with a hematocrit of 25 on evaluation at "
    """.strip(),
    'Unsure',
    """
    Context: "HEMOGLOBIN A1C, WB               6.1                       (3.9-6.1)      %"
    """.strip(),
    '6.1',
    """
    Context: "-check A1c."
    """.strip(),
    'Unsure',
    """
    Context: "Last HgbA1c was in October and was 7.7 which is a moderate improvement for him."
    """.strip(),
    '7.7',
    """
    Context: "A1c over 9%. She still has trouble focusing on it."
    """.strip(),
    '9.0',
    """
    Context: "A1Cs – 7.70% in 3/2113, 7.60% in 2112, 10.10% in 2111, 10.70% in 2106, 9.80% in 2104"
    """.strip(),
    '7.7',
    """
    Context: "LABORATORY EVALUATION:  CBC:  White count 8.9, hematocrit 40.8, "
    """.strip(),
    'Unsure'
]

example_dictionary = {
    "example_A": example_A,
    "example_B": example_B,
    "example_C": example_C,
    "example_D": example_D,
    "example_E": example_E,
    "vicuna_13b_fine_tuned": vicuna_13b_fine_tuned
}