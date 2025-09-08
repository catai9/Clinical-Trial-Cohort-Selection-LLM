prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has osteoarthritis (OA)? Answer Yes, No, Maybe, or Unmentioned to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "OTHER DIAGNOSIS;Conditions , Infections , Complications , affecting Treatment/Stay s/p cardiac transplant htn obesity CRI gout ( gout ) s/p ccy ( S/P cholecystectomy ) pulm amiodarone toxicity"
    """.strip(),
    "Answer: The text does not mention if the patient has osteoarthritis (OA). So the answer is Unmentioned.",
    '''
    Context: " HTN , obesity , anemia , OA , gout , GERD , CRI , CAD , hyperlipidemia"
    '''.strip(),
    "Answer: The text mentions that the patient has osteoarthritis (OA). So the answer is Yes.",
    '''
    Context: "Echo was repeated this admit which showed EF 60-65% and signs of diastolic dysfunction."
    '''.strip(),
    "Answer: The text does not mention if the patient has osteoarthritis (OA). So the answer is Unmentioned.",
    '''
    Context: "PAST MEDICAL HISTORY: His pat medical history is significant for a duodenal ulcer ( upper GI bleed , 1988 ) , ankylosing spondylitis , adult onset diabetes mellitus , juvenile rheumatoid arthritis , hyperglyceremia , hypertension."
    '''.strip(),
    "Answer: The text does not mention if the patient has osteoarthritis (OA). So the answer is Unmentioned.",
    '''
    Context: "PAST MEDICAL HISTORY: TIA , extremity weakness of the right side , which was transient and has since resolved , CVA in 1994 without residual weakness , chronic renal insufficiency , gunshot wound to his chest and head at the age of 14 , hepatitis B , and gout."
    '''.strip(),
    "Answer: The text does not mention if the patient has osteoarthritis (OA). So the answer is Unmentioned.",
    '''
    Context: "SECONDARY DIAGNOSES: 1 ) HYPERCOAGULABILITY state WITH NEGATIVE SERUM WORK-UP. 2 ) RULE OUT RENAL CELL CARCINOMA ON THE LEFT ( CT PENDING ). 3 ) HISTORY OF PPD POSITIVITY WITH CHEST X-RAY NEGATIVE. 4 ) GOUT."
    '''.strip(),
    "Answer: The text does not mention if the patient has osteoarthritis (OA). So the answer is Unmentioned.",
]

example_dictionary = {
    "example_A": example_A
}