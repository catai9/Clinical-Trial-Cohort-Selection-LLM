prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has excessive alcohol use? Answer Yes or No to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "Social History: 40 pack-years, 2-3 EtOH drink/week, lives alone."
    """.strip(),
    'Answer: The text mentions 2-3 drink/week. 2-3 drink/week is considered occasional alcohol use. Occasional alcohol use is not considered as alcohol abuse. So the answer is No.',
    """
    Context: "25%, and this is thought to be due to alcoholic cardiomyopathy"
    """.strip(),
    "Answer: The text does not mention the patient's current alcohol use. So the answer is No.",
    """
    Context: "He does not drink."
    """.strip(),
    'Answer: The text mentions the person does not drink. So the answer is No.',
    """
    Context: "5-6 beers/night on wkends; last drink last Sunday; no h/o withdrawal or seizures"
    """.strip(),
        'Answer: The text mentions 5-6 drinks each night which is considered excessive alcohol use. So the answer is Yes.',
    """
    Context: "He has a heavy ETOH history in the past that he reduced to a beer or martini every day in the past few years."
    """.strip(),
    'Answer: The text mentions a heavy history of alcohol use in the past, but the current alcohol use is a drink every day. Occasional alcohol use is not considered as alcohol abuse. So the answer is No.'
]

example_B = [prompt + 
    """
    Context: "Tobacco - 50 pack year, currently 1/2 pack per day, had recently quit for 4 weeks but restarted due to &#8220;stress&#8221;.  Tried to start Chantix, but insurance does not cover."
    """.strip(),
    "Answer: The text does not mention the patient's current alcohol use. So the answer is No.",
    """
    Context: "His wife is concerned about the amount of alcohol he was drinking and Dr. Jaimes for a second opinion and was advised to exercise more and cut down on alcohol. ALCOHOL   Reiterate the importance of keeping limit on alcohol."
    """.strip(),
    "Answer: The text mentions the patient drinks a concerning amount of alcohol. So the answer is Yes.",
    """
    Context: "She denies alcohol, intravenous Alcohol-social only"
    """.strip(),
    'Answer: The text mentions the person does not drink. So the answer is No.',
    """
    Context: "No alcohol use"
    """.strip(),
    'Answer: The text mentions the person does not drink. So the answer is No.',
     """
    Context: "5-6 beers/night on wkends; last drink last Sunday; no h/o withdrawal or seizures"
    """.strip(),
    'Answer: The text mentions 5-6 drinks each night which is considered excessive alcohol use. So the answer is Yes.'
]

example_C = [prompt + 
    """
    Context: "Tobacco: Quit 2062; ETOH: None; Caffeine: 1-2 cups/day; Exercise: Very limited since discharge."
    """.strip(),
    "Answer: The text mentions the patient does not drink alcohol. So the answer is No.",
    """
    Context: "Depression   + ETOH dependence"
    """.strip(),
    "Answer: The text mentions the patient has alcohol dependence. So the answer is Yes.",
    """
    Context: "Risks: Never use tobacco, rarely used alcohol, no injection drug use"
    """.strip(),
    'Answer: The text mentions the patient rarely uses alcohol. So the answer is No.',
    """
    Context: "SOCIAL HISTORY:  Past tobacco use, occasional ETOH, no IV drug"
    """.strip(),
    'Answer: The text mentions the patient has alcohol occasionally. So the answer is No.',
     """
    Context: "When he's depressed he becomes a binge drinker."
    """.strip(),
    'Answer: The text mentions that the patient becomes a binge drinker when he\'s depressed. So the answer is Yes.'
]

example_D = [prompt + 
    """
    Context: " He mentions that he does not drink alcohol and quit smoking 20 years ago after having smoked 2 cigars/day for 20yrs. He denies using illicit drugs."
    """.strip(),
    "Answer: The text mentions the patient does not drink alcohol. So the answer is No.",
    """
    Context: "His wife is concerned about the amount of alcohol he was drinking and Dr."
    """.strip(),
    "Answer: The text mentions the patient drinks a concerning amount of alcohol. So the answer is Yes.",
    """
    Context: "The text mentions the patient drinks alcohol rarely, a glass of wine maybe once a week, one cup of soda with caffeine each day."
    """.strip(),
    'Answer: The text mentions the person drinks alcohol rarely, a glass of wine maybe once a week, and one cup of soda with caffeine each day. So the answer is No.',
    """
    Context: "EtOH: unknown"
    """.strip(),
    'Answer: The text mentions there is no history of tobacco or alcohol use. So the answer is No.',
     """
    Context: "Did drink significantly in the past, but usually only on the weekends, but did not drink everyday. He has not had anything to drink since he started his chemotherapy regiment."
    """.strip(),
    'Answer: The text mentions the patient used to drink alcohol but currently does not have excessive alcohol use. So the answer is No.'
]

example_E = [prompt + 
    """
    Context: "No EtOH. No drugs"
    """.strip(),
    "Answer: The text mentions the patient does not drink alcohol. So the answer is No.",
    """
    Context: " Alcohol use: 3-4beers/day. He does not smoke, drinks alcohol socially, and denies illicit drug use."
    """.strip(),
    "Answer: The text mentions the patient only drinks alcohol socially, about 3-4 beers/day. So the answer is No.",
    """
    Context: "Alcohol:  The patient drinks and with no history of alcohol withdrawal or seizures.  5-6 beers per night on weekends with her last drink many days ago"
    """.strip(),
    'Answer: The text mentions the patient drinks 5-6 beers per night on weekends, with no history of alcohol withdrawal or seizures. So the answer is Yes.',
    """
    Context: "I have told her to eat a banana during the evening and possibly this would avoid leg cramps in the evening."
    """.strip(),
    'Answer: The text does not mention the patient\'s current alcohol use. So the answer is No.',
     """
    Context: "Social History:   40 pack-years, 2-3 EtOH drink/week, lives alone."
    """.strip(),
    'Answer: The text mentions the patient has 2-3 drinks of alcohol per week. So the answer is No.'
]

vicuna_13b_fine_tuned = ["Here are a few ways of naming alochol: {}".format('alcohol,binge,DUI') + "\n\n" + """
                Now, these are some sentences from a patient's clinical report. Does the patient currently abuse alcohol? Let's think step by step.
                """.strip() + "\n\n" + """
    Context: "Social History: 40 pack-years, 2-3 EtOH drink/week, lives alone."
    """.strip(),
    'Answer: The text mentions 2-3 drink/week. 2-3 drink/week is considered occasional alcohol use. Occasional alcohol use is not considered as alcohol abuse. So the answer is No.',
    """
    Context: "Occ EtOH; no cocaine, any illicit drug use."
    """.strip(),
    'Answer: The text mentions occasional alcohol use. Occasional alcohol use is not considered as alcohol abuse. So the answer is No.',
    """
    Context: "25%, and this is thought to be due to alcoholic cardiomyopathy"
    """.strip(),
    "Answer: The text does not mention the patient's current alcohol use. So the answer is No.",
    """
    Context: "He does not drink."
    """.strip(),
    'Answer: The text states the person does not drink. So the answer is No.',
    """
    Context: "5-6 beers/night on wkends; last drink last Sunday; no h/o withdrawal or seizures"
    """.strip(),
    'Answer: The text mentions 5-6 drinks each night which is considered excessive alcohol use. So the answer is Yes.',
    """
    Context: "He has a heavy ETOH history in the past that he reduced to a beer or martini every day in the past few years."
    """.strip(),
    'Answer: The text mentions a heavy history of alcohol use in the past, but the current alcohol use is a drink every day. Occasional alcohol use is not considered as alcohol abuse. So the answer is No.',
    """
    Context: "Smoking status 01/17/2112  Current smoker  Last Counsel date: 01/17/2112, No Of Cigarettes Smoked per Day: 10-19 CIG/DAY (1/2-1 ppd), Readiness to Change: Ready to quit now"
    """.strip(),
    "Answer:  The text mentions smoking usage. Smoking is not related to alcohol use. The text does not mention the patient's current alcohol use. So the answer is No.",
    """
    Context: "MS: disorganized thought (s/p ativan), speech fluent, flat affect"
    """.strip(),
    "Answer:  The text does not mention the patient's current alcohol use. So the answer is No.",
    """
    Context: "Father w/ EtOH, HTN."
    """.strip(),
    "Answer:  The text does not mention the patient's current alcohol use. So the answer is No.",
    """
    Context: "the pain is a burning pain - as if someone poured alcohol on the spot. pain travels down the right leg"
    """.strip(),
    "Answer:  The text does not mention the patient's current alcohol use. So the answer is No.",
    """
    Context: "Prior h/o heavy ETOH and tob."
    """.strip(),
    "Answer: The text mentions past alcohol consumption. The text does not mention the patient's current alcohol use. So the answer is No.",
    """
    Context: "Alcohol use: 3-4 beers/d until 8 years ago for 30 years"
    """.strip(),
    "Answer: The text mentions a heavy history of alcohol use in the past. The text does not mention the patient's current alcohol use. So the answer is No.",
    """
    Context: "Tobacco abuse"
    """.strip(),
    "Answer: The text mentions tobacco abuse. Tobacco abuse is not related to alcohol use. The text does not mention the patient's current alcohol use. So the answer is No.",
    """
    Context: "He is a recovering alcoholic."
    """.strip(),
    "Answer: The text mentions that the patient is a recovering alcoholic. The text does not mention the patient's current alcohol use. So the answer is No.",
    """
    Context: "Did manage to stop for 1 year, started again due to pressure/anxiety.<BR>Alcohol: none.<BR>Just lost his job as a veterinary aide - pt feels this was due to his elevated BG, has called in sick a few times, sometimes very sleepy.<BR>Lives alone.<BR>"
    """.strip(),
    "Answer: The text mentions that the alcohol consumption is none for the patient. This means the person does not drink. So the answer is No.",
    """
    Context: "HPI - 67 yo m c h/o htn, heavy EtOH use, and smoking who presented on 10/12/70 to LGH c CP."
    """.strip(),
    "Answer: The text mentions heavy EtOH use in the past. The text does not mention the patient's current alcohol use. So the answer is No.",
    """
    Context: "The patient's alcohol intake may be excessive."
    """.strip(),
    "Answer: The text mentions that the patient's alcohol intake may be excessive but is not certain. So the answer is No.",
    """
    Context: "-obtain collateral history regarding possible alcohol abuse and monitor for alcohol withdrawal"
    """.strip(),
    "Answer: The text does not mention the patient's current alcohol use. So the answer is No.",
    """
    Context: "Caffeine: 5-6/day (coffee and diet coke)"
    """.strip(),
    "Answer: The text mentions caffeine use. Caffeine use is not related to alcohol use. The text does not mention the patient's current alcohol use. So the answer is No.",
    """
    Context: "He said he has cut his alcohol back to 6 pack once a week."
    """.strip(),
    "Answer:  The text mentions that the patient has cut back on alcohol to 6 packs once a week. 6 packs per week is considered occasional alcohol use. Occasional alcohol use is not considered as alcohol abuse. So the answer is No.",
    """
    Context: "Although he denied illicit drug use, his chart review revealed above noted history of cocaine abuse."
    """.strip(),
    "Answer: The text mentions cocaine abuse. Cocaine abuse is not related to alcohol use. The text does not mention the patient's current alcohol use. So the answer is No."
    """
    Context: "10) TOBACCO USE: Nora reported quitting at last visit but today smelled of smoke."
    """.strip(),
    "Answer: The text mentions tobacco use. Tobacco use is not related to alcohol use. The text does not mention the patient's current alcohol use. So the answer is No."
    """
    Context: "Alcohol:  None, h/o ETOH abuses"
    """.strip(),
    "Answer: The text mentions a history of alcohol abuse in the past, but the current alcohol use is none. So the answer is No."
]

example_dictionary = {
    "example_A": example_A,
    "example_B": example_B,
    "example_C": example_C,
    "example_D": example_D,
    "example_E": example_E,
    "vicuna_13b_fine_tuned": vicuna_13b_fine_tuned
}