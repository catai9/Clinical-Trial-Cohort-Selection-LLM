prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has gallstones? Answer Yes, No, or Unsure to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "BUN/creatinine 34/0.9 , liver function tests within normal limits ,"
    """.strip(),
    "Answer: The text does not mention that the patient has gallstones. So the answer is No.",
    '''
    Context: "Cholecystectomy in 1986. 4. Lysis of adhesions for small bowel obstruction in 1970 , repeated in 1970 again. 5. Resection of a herniated nucleus pulposus in 1985. 6. Knee operation in 1974. 7."
    '''.strip(),
    "Answer: The text mentions that the patient had a cholecystectomy. A cholecystectomy removes the gallbladder. Gallstones are a common condition that can form in the gallbladder and can cause pain, inflammation, and other complications. It is likely that the patient had a cholecystectomy to remove gallstones. So the answer is Yes.",
    '''
    Context: "EF of 10% to 15% , MI , diabetes mellitus , hypertension , hypothyroidism , status post cholecystectomy for cholelithiasis , and a history of probable prostate ??___??."
    '''.strip(),
    "Answer: The text mentions that the patient has a history of cholecystectomy for cholelithiasis.  had surgery to remove their gallbladder due to the presence of gallstones. So the answer is Yes.",
    '''
    Context: "PAST MEDICAL HISTORY: Significant for hypercholesterolemia , pulmonary embolism in 1987 ,"
    '''.strip(),
    "Answer: The text does not mention that the patient has gallstones. So the answer is No.",
    '''
    Context: "Non-contrast CT of the abdomen showed biliary sludge and gallstones , no evidence of acute cholecystitis."
    '''.strip(),
    "Answer: The text mentions that the patient has gallstones. So the answer is Yes.",
    '''
    Context: "WC-dependent. 9. Chronic anemia secondary to chronic kidney disease."
    '''.strip(),
    "Answer: The text does not mention that the patient has gallstones. So the answer is No.",
    '''
    Context: "Instructions: if gallbladder still in- start taking 2 weeks after discharge"
    '''.strip(),
    "Answer: The text does not mention that the patient has gallstones. So the answer is No.",
]

example_dictionary = {
    "example_A": example_A
}