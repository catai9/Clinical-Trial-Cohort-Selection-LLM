prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient used illicit drugs in the past? Answer Yes or No to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "Illicit drugs: The patient denies past and present use of illicit drugs."
    """.strip(),
    'Answer: The text mentions the patient does not use illicit drugs. So the answer is No.',
    """
    Context: "Drugs: previous use of cocaine and pot in HS"
    """.strip(),
    'Answer: The text mentions the patient previously used cocaine and pot. Cocaine and pot are illicit drugs. So the answer is Yes.',
    """
    Context: "SOCIAL HISTORY:  She does not smoke or use street drugs. She does not do drugs."
    """.strip(),
    'Answer: The text mentions the patient does not use illicit drugs. So the answer is No.',
    """
    Context: "ALCOHOL Reiterate the importance of keeping limit on alcohol."
    """.strip(),
    'Answer: The text mentions keeping a limit on alcohol. Alcohol use is not correlated with drug use. So the answer is No.'
]

example_B = [prompt + 
    """
    Context: "He denies using illicit drugs."
    """.strip(),
    'Answer: The text mentions the patient does not use illicit drugs. So the answer is No.',
    """
    Context: "Although he denied illicit drug use, his chart review revealed above noted history of cocaine abuse."
    """.strip(),
    'Answer: The text mentions the patient previously used cocaine. Cocaine is an illicit drug. So the answer is Yes.',
    """
    Context: "Her only medication is lente insulin taken twice per day."
    """.strip(),
    'Answer: The text mentions the patient does not use illicit drugs. So the answer is No.',
    """
    Context: "H/O DRUG ABUSE"
    """.strip(),
    'Answer: The text mentions the patient has a history of drug abuse. So the answer is Yes.'
]

example_C = [prompt + 
    """
    Context: "Based on exam, suspect a combination of CHF and pleural effusions (diuretic medication was not being taken at prescribed dose accidentally)."
    """.strip(),
    'Answer: The text does not mention the patient used illicit drugs. So the answer is No.',
    """
    Context: "OXYCODONE   5 MG (5MG TABLET take 1) PO Q4H PRN pain , Please do not drink and/or drive while taking narcotics."
    """.strip(),
    'Answer: The text mentions the patient is taking Oxycodone, which is a prescription opioid medication. However, it does not mention the use of illicit drugs. So the answer is No.',
    """
    Context: "H/O drug abuse : IV drug user stopped heroin 2 years ago-methadone 95 mg per day."
    """.strip(),
    'Answer: The text mentions the patient has a history of drug abuse. So the answer is Yes.',
    """
    Context: "There is a previous use of cocaine in high school but no drug use currently. Drugs: previous use of cocaine and pot in HS"
    """.strip(),
    'Answer: The text mentions the patient has a history of drug abuse. So the answer is Yes.'
]

example_D = [prompt + 
    """
    Context: "ALLERGIES:  No known drug allergies."
    """.strip(),
    "Answer: The text does not mention the patient used illicit drugs. So the answer is No.",
    """
    Context: "Drugs - none"
    """.strip(),
    "Answer: The text mentions the patient does not use drugs. So the answer is No.",
    """
    Context: "Although he denied illicit drug use, his chart review revealed above noted history of cocaine abuse."
    """.strip(),
    'Answer: The text mentions that the patient has a history of cocaine abuse. So the answer is Yes.',
    """
    Context: "He does not smoke, drinks alcohol socially, and denies illicit drug use."
    """.strip(),
    'Answer: The text mentions the patient does not use illicit drugs. So the answer is No.'
]

example_E = [prompt + 
    """
    Context: "Please see resident note for list of medication and allergies."
    """.strip(),
    "Answer: The text does not mention the patient using illicit drugs. So the answer is No.",
    """
    Context: "Zocor (SIMVASTATIN) 80 MG (80MG TABLET take 1) PO QHS x 30 days, if you develop muscle pain or weakness, stop the drug immediately and call your doctor."
    """.strip(),
    "Answer: The text does not mention the patient using illicit drugs. So the answer is No.",
    """
    Context: "-IVDU: no IVDU; used marijuana in the past"
    """.strip(),
    'Answer: The text mentions the patient used marijuana in the past. Marijuana is an illicit drug. So the answer is Yes.',
    """
    Context: "H/O DRUG ABUSE"
    """.strip(),
    'Answer: The text mentions the patient has a history of drug abuse. So the answer is Yes.'
]

vicuna_13b_fine_tuned = ["These are some sentences from a patient's clinical report. Does the text mention that the patient used illicit drugs in the past? Let's think step by step.""".strip()  + "\n\n" + """
    Context: "Illicit drugs: The patient denies past and present use of illicit drugs."
    """.strip(),
    'Answer: The text states the patient does not use illicit drugs. So the answer is No.',
    """
    Context: "Drugs: previous use of cocaine and pot in HS"
    """.strip(),
    'Answer: The text states the patient previously used cocaine and pot. Cocaine and pot are illicit drugs. So the answer is Yes.',
    """
    Context: "SOCIAL HISTORY:  She does not smoke or use street drugs. She does not do drugs."
    """.strip(),
    'Answer: The text states the patient does not use illicit drugs. So the answer is No.',
    """
    Context: "Alcohol/Illicit/IV Drugs - History of cocaine and EtOH abuse clean x 14 yrs"
    """.strip(),
    'Answer: The text states the patient previously used cocaine. Cocaine is an illicit drug. So the answer is Yes.',
    """
    Context: "-IVDU: no IVDU; used marijuana in the past"
    """.strip(),
    'Answer: The text states that the patient used marijuana in the past. Marijuana is an illicit drug. So the answer is Yes.',
    """
    Context: "H/O DRUG ABUSE"
    """.strip(),
    'Answer: The text states that the patient has a history of drug abuse. So the answer is Yes.',
    """
    Context: "+occasional marijuana."
    """.strip(),
    'Answer: The text states that the patient uses occasional marijuana. Marijuana is an illicit drug. So the answer is Yes.',
    """
    Context: "Drugs:  None"
    """.strip(),
    'Answer: The text states that the patient does not use drugs. So the answer is No.',
    """
    Context: "SOCIAL HISTORY:  He is not a smoker, drinker, or drug user."
    """.strip(),
    'Answer: The text states that the patient does not use drugs. So the answer is No.',
    """
    Context: "He denies using illicit drugs."
    """.strip(),
    'Answer: The text mentions that the patient denies using illicit drugs. So the answer is No.',
    """
    Context: Context: "No drugs"
    """.strip(),
    'Answer: The text mentions that there are no drugs. So the answer is No.',
    """
    Context: "ALCOHOL   Reiterate the importance of keeping limit on alcohol.
    """.strip(),
    'Answer: The text mentions keeping a limit on alcohol. Alcohol use is not correlated with drug use. So the answer is No.',
    """
    Context: "has no known drug allergies."
    """.strip(),
    "Answer: The text mentions no known drug allergies. The text not does mention the patient's use of illicit drugs. So the answer is No.",
    """
    Context: "He quit smoking 30 years ago and denies alcohol use."
    """.strip(),
    "Answer: The text does not mention the patient's use of illicit drugs. So the answer is No."
]

example_dictionary = {
    "example_A": example_A,
    "example_B": example_B,
    "example_C": example_C,
    "example_D": example_D,
    "example_E": example_E,
    "vicuna_13b_fine_tuned": vicuna_13b_fine_tuned
}