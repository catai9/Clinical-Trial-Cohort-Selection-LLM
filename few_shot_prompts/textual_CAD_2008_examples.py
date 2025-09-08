prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has atherosclerotic CV disease (CAD)? Answer Yes, No, Maybe, or Unmentioned to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "HPI: 75F with iCMP , CAD s/p MI s/p multiple stents to LAD , LCx"
    """.strip(),
    "Answer: The text mentions that the patient has atherosclerotic CV disease (CAD). So the answer is Yes.",
    '''
    Context: "She was ruled out for a myocardial infarction and had an exercise tolerance test which was negative for ischemic disease."
    '''.strip(),
    "Answer: The text does not mention if the patient has atherosclerotic CV disease (CAD). So the answer is Unmentioned.",
    '''
    Context: "HISTORY OF PRESENT ILLNESS: Patient is a 79 year old Russian speaking female who had had a history of exertional chest pain and no previous documented coronary artery disease."
    '''.strip(),
    "Answer: The text mentions that the patient does not have a history of atherosclerotic CV disease (CAD). So the answer is No.",
    '''
    Context: "List: CV-I: ? h/o of CAD by previous stress test; nNZ's"
    '''.strip(),
    "Answer: The text has a question mark in front of history of atherosclerotic CV disease (CAD). It is unclear from the question mark if the patient has or does not have CAD. So the answer is Maybe.",
    '''
    Context: "Given the patient's history of atherosclerosis , further imaging of the abdominal vessels by MRA during followup was recommended by the GI Service."
    '''.strip(),
    "Answer: The text does not mention if the patient has atherosclerotic CV disease (CAD). So the answer is Unmentioned.",
    '''
    Context: "OTHER DIAGNOSIS;Conditions , Infections , Complications , affecting Treatment/Stay htn ( hypertension ) obesity ( obesity ) h/o sarcoid ( H/O sarcoid ) arthritis ( polyarticular arthritis ) diverticulosis ( diverticulosis ) ventral hernia depression ( depression ) unstable angina ( angina ) HPI: 49 yo woman cx h/o recurrent chest pain concerning for unstable angina but c clean catheterization 2/17 p/w SSCP."
    '''.strip(),
    "Answer: The text does not mention if the patient has atherosclerotic CV disease (CAD). So the answer is Unmentioned.",
    '''
    Context: "CAD , HTN , hyperlipidemia , PVD , tinnitus , NIDDM , osteoarthritis 102963848 | OFEMC | 02256361 | | 9387575 | 8/16/2004 12:00:00 AM | Left carotid stenosis | | DIS | Admission Date: 10/10/2004 Report Status:"
    '''.strip(),
    "Answer: The text mentions that the patient has atherosclerotic CV disease (CAD). So the answer is Yes.",
]

example_dictionary = {
    "example_A": example_A
}