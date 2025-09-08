prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has gastroesophageal reflux disease (GERD)? Answer Yes, No, or Unsure to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "Other valvular function appeared to be within normal limits with exception of moderate-to-severe tricuspid regurgitation and peak systolic pulmonary artery pressures of 31 mmHg plus right atrial pressure. "
    """.strip(),
    "Answer: The text mentions that the patient experiences moderate-to-severe tricuspid regurgitation. Tricuspid regurgitation is a key symptom of gastroesophageal reflux disease (GERD). So the answer is Yes.",
    '''
    Context: "Take consistently with meals or on empty stomach."
    '''.strip(),
    "Answer: The text does not mention that the patient has gastroesophageal reflux disease (GERD). So the answer is No.",
    '''
    Context: "It also noted mitral valve had moderate to severe mitral regurgitation."
    '''.strip(),
    "Answer: The text mentions that the patient experiences moderate to severe mitral regurgitation. Mitral regurgitation is a key symptom of gastroesophageal reflux disease (GERD). So the answer is Yes.",
    '''
    Context: "ZANTAC SYRUP ( RANITIDINE HCL SYRUP ) 150 MG PO BID"
    '''.strip(),
    "Answer: The text mentions the patient being prescribed Zantac syrup (ranitidine hydrochloride syrup) at a dose of 150 mg PO BID, which is a medication commonly used to treat gastroesophageal reflux disease (GERD). However, the text does not explicitly mention that the patient has GERD. So the answer is Unsure.",
    '''
    Context: "RANITIDINE HCL 150 MG PO BID Likely restrictive component due to obesity as well as deconditioning , likely anxiety component as well as possible pulmonary hypertension due to sleep apnea , smoking hx."
    '''.strip(),
    "Answer: The text does not mention that the patient has gastroesophageal reflux disease (GERD). So the answer is No.",
    '''
    Context: "Abdominal computerized tomography scan showed some thickening and some mild edema of her bowel wall , and moderate to large amount of ascites with no evidence of perforation."
    '''.strip(),
    "Answer: The text does not mention that the patient has gastroesophageal reflux disease (GERD). So the answer is No.",
]

example_dictionary = {
    "example_A": example_A
}