prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has obesity? Answer Yes, No, or Unsure to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "This is a 77-year-old woman with a history of diabetes mellitus , obesity , and hyperlipidemia as well as peripheral vascular disease who has had progressively worsening dyspnea on exertion."
    """.strip(),
    "Answer: The text mentions that the patient has obesity. So the answer is Yes.",
    '''
    Context: "The patient's insulin regimen can be adjusted as an outpatient and possibly oral diabetes medications restarted."
    '''.strip(),
    "Answer: The text does not mention that the patient has obesity. So the answer is No.",
    '''
    Context: "Upon admission , height 5 feet 10 inches , weight 102 kg , heart rate of 54 , blood pressure 130/88 in the right arm and 142/88 in the left arm. "
    '''.strip(),
    "Answer: The text mentions that the patient has a height of 5 feet 10 inches or 1.728 meters and a weight of 102 kg. Obesity is defined as having a body mass index (BMI) of 30 or higher. Using the patient's height and weight, the BMI is calculated as BMI = weight (kg) / (height (m))^2. Using the patient's values, their BMI is 102 / (1.728)^2 or 36.1. The patient's BMI is 36.1 which is higher than the threshold for obesity. So the answer is Yes.",
    '''
    Context: "71 y/o woman w/ hx of GERD , ?anginal pain , DM , HTN , asthma , DJD , gastroparesis admitted with two episodes of chest pain on the night PTA relieved by nitroglycerin."
    '''.strip(),
    "Answer: The text does not mention that the patient has obesity. So the answer is No.",
    '''
    Context: "The patient's dry weight is 57 kg."
    '''.strip(),
    "Answer: The text mentions that the patient's weight at discharge was 61 kg. Obesity is defined as having a body mass index (BMI) of 30 or higher. Using the patient's weight and height, the BMI can be calculated as BMI = weight (kg) / (height (m))^2. The text does not provide the patient's height, so the BMI cannot be calculated. So the answer is No.",
    '''
    Context: "PAST MEDICAL HISTORY: His pat medical history is significant for a duodenal ulcer ( upper GI bleed , 1988 ) , ankylosing spondylitis , adult onset diabetes mellitus , juvenile rheumatoid arthritis , hyperglyceremia , hypertension."
    '''.strip(),
    "Answer: The text does not mention that the patient has obesity. So the answer is No.",
]

example_dictionary = {
    "example_A": example_A
}