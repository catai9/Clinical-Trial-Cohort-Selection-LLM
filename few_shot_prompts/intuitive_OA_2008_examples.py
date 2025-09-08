prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has osteoarthritis (OA)? Answer Yes, No, or Unsure to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "morbid obesity , left knee degenerative joint disease , iron-deficiency anemia."
    """.strip(),
    "Answer: The text mentions that the patient has left knee degenerative joint disease. Degenerative joint disease is a type of osteoarthritis (OA). So the answer is Yes.",
    '''
    Context: "Includes chronic venous stasis ulcers in lower extremities , diabetes mellitus , hypertension , asthma , sarcoid , restricted pulmonary disease , and obesity."
    '''.strip(),
    "Answer: The text does not mention that the patient has osteoarthritis (OA). So the answer is No.",
    '''
    Context: "Dyslipidemia ( dyslipidemia ) DJD spine ( OA of cervical spine ) Hx vocal cord injury postop Hx gastritis with UGIB ( H/O upper"
    '''.strip(),
    "Answer: The text mentions that the patient has osteoarthritis (OA) of the cervical spine. So the answer is Yes.",
    '''
    Context: "Pt. in her USOH , eating potato chips at home , when she had palpitations for a couple of minutes , +LH , felt weak , SOB , then had tightness in chest which she has never had before with her palpitations."
    '''.strip(),
    "Answer: The text does not mention that the patient has osteoarthritis (OA). So the answer is No.",
    '''
    Context: "PAST MEDICAL HISTORY: His pat medical history is significant for a duodenal ulcer ( upper GI bleed , 1988 ) , ankylosing  spondylitis , adult onset diabetes mellitus , juvenile rheumatoid arthritis , hyperglyceremia , hypertension."
    '''.strip(),
    "Answer: The text does not mention that the patient has osteoarthritis (OA). So the answer is No.",
    '''
    Context: "ALLERGIES: Patient had no known drug allergies ( hydrochlorothiazide was thought to cause gout exacerbations and ace inhibitor thought to cause cough , and beta blocker with urinary retention )."
    '''.strip(),
    "Answer: The text does not mention that the patient has osteoarthritis (OA). So the answer is No.",
    '''
    Context: "PAST MEDICAL HISTORY: Significant for hypercholesterolemia , pulmonary embolism in 1987 , peripherovascular disease in the 70's , non-insulin dependent diabetes , history of hepatitis B , and left shoulder fracture."
    '''.strip(),
    "Answer: The text does not mention that the patient has osteoarthritis (OA). So the answer is No.",
]

example_dictionary = {
    "example_A": example_A
}