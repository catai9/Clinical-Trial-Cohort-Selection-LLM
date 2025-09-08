prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient has major diabetes-related complication? "Major complication" (as opposed to "minor complication") is defined as any of the following that are a result of (or strongly correlated with) uncontrolled diabetes: Amputation, Kidney damage, Skin conditions, Retinopathy, Nephropathy, and Neuropathy. Answer Yes or No to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "No skin changes. Monitor UOP for kidney functions. Neuro/Psych: No numbness, tingling, pain, loss of coordination or balance, weakness, or loss of memory."
    """.strip(),
    'Answer: The text makes no mention of the patient having major diabetes-related complications (Amputation, Kidney damage, Skin conditions, Retinopathy, Nephropathy, and Neuropathy). So the answer is No.',
    """
    Context: "50 yo F diabetic with active smoking and peripheral vascular disease, now with wet gangrene of L great toe. She is now admitted for parenteral antibiotics and amputation of the L great toe and debridement of the R forefoot ulcer." 
    """.strip(),
    'Answer: The text mentions that the patient is a diabetic who will receive amputation. Amputation is considered one of the "major complications". So the answer is Yes.',
    """
    Context: "His recent vascular studies showed no significant drop off and perfusion pressures level of the ankle."
    """.strip(),
    'Answer: The text makes no mention of the patient having major diabetes-related complications (Amputation, Kidney damage, Skin conditions, Retinopathy, Nephropathy, and Neuropathy). So the answer is No.',
    """
    Context: "Her known diabetic complications include retinopathy with prior photocoagulopathy, nephropathy with microalbuminuria, neuropathy with intermittent numbness and tingling at night in feet, and no known macrovascular disease. 4)	nephropathy"
    """.strip(),
    'Answer: The text mentions that the patient has retinopathy, nephropathy, and neuropathy. Retinopathy, nephropathy, and neuropathy are considered "major complications". So the answer is Yes.'
]

example_B = [prompt + 
    """
    Context: "Musco/skel/Skin: Has arthritis. No skin changes."
    """.strip(),
    'Answer: The text makes no mention of the patient having major diabetes-related complications (Amputation, Kidney damage, Skin conditions, Retinopathy, Nephropathy, and Neuropathy). So the answer is No.',
    """
    Context: "Her known diabetic complications include retinopathy with prior photocoagulopathy, nephropathy with microalbuminuria, neuropathy with intermittent numbness and tingling at night in feet, and no known macrovascular disease." 
    """.strip(),
    'Answer: The text mentions that the patient has retinopathy. Retinopathy is considered one of the "major complications". So the answer is Yes.',
    """
    Context: "Neurological: peripheral neuropathy from knees down to feet bilaterally plus edema; bilateral carpal tunnel"
    """.strip(),
    'Answer: The text mentions that the patient has neuropathy. Neuropathy is considered one of the "major complications". So the answer is Yes.',
    """
    Context: "Otherwise, no active synovitis or skin lesions. no photosensitivity but she does have some oral ulcers and Raynaud's. She"
    """.strip(),
    'Answer: The text makes no mention of the patient having major diabetes-related complications (Amputation, Kidney damage, Skin conditions, Retinopathy, Nephropathy, and Neuropathy). So the answer is No.'
]

example_C = [prompt + 
    """
    Context: "Skin: no rashes/sores, good skin turgor."
    """.strip(),
    'Answer: The text makes no mention of the patient having major diabetes-related complications (Amputation, Kidney damage, Skin conditions, Retinopathy, Nephropathy, and Neuropathy). So the answer is No.',
    """
    Context: "CM/CAD as described, Hypertension, Type II DM x 15 yrs- with nephropathy, neuropathy and retinopathy, Mild renal insufficiency, PVD, Carotid disease, Factor VII Deficiency, BPH, Hearing loss, Vitamin B12 deficiency." 
    """.strip(),
    'Answer: The text mentions that the patient has nephropathy. Nephropathy is considered one of the "major complications". So the answer is Yes.',
    """
    Context: "PMHx: DM, HTN, dementia, h/o sz d/o not on AED now, Pituitary adenoma, s/p hypophysectomy, hypothyroidism, COPD, dyslipidemia, obesity, fatty liver, fibromyalgia, arthritis, depression, anxiety, meningitis, Rt humerus fx/osteo/nonunion, Cirrhosis or unclear etiology with hyperammonemia, Neuropathy with paresthesias, presumably due to diabetes"
    """.strip(),
    'Answer: The text mentions that the patient has neuropathy. Neuropathy is considered one of the "major complications". So the answer is Yes.',
    """
    Context: "HPI: 84 yo F, with known mesenteric ischemia, who was recently hospitalized 1/18/88-1/30/88 with influenza A, demand cardiac ischemia, and an E. coli UTI."
    """.strip(),
    'Answer: The text makes no mention of the patient having major diabetes-related complications (Amputation, Kidney damage, Skin conditions, Retinopathy, Nephropathy, and Neuropathy). So the answer is No.'
]

example_D = [prompt + 
    """
    Context: "HEENT: R eye not reactive to light; L eye 3  2mm with light; EOMI"
    """.strip(),
    "Answer: The text makes no mention of the patient having major diabetes-related complications (Amputation, Kidney damage, Skin conditions, Retinopathy, Nephropathy, and Neuropathy). So the answer is No.",
    """
    Context: "Impression   52F with poorly controlled type II DM and known neuropathy, nephropathy, retinopathy and gastroparesis, repeated admission for nausea, vomiting, poor nutrition."
    """.strip(),
    "Answer: The text mentions that the patient has nephropathy. Nephropathy is considered one of the \"major complications\". So the answer is Yes.",
    """
    Context: "We will also repeat the chest CT scan to make sure she has not suffered from recurrent pulmonary embolism."
    """.strip(),
    'Answer: The text makes no mention of the patient having major diabetes-related complications (Amputation, Kidney damage, Skin conditions, Retinopathy, Nephropathy, and Neuropathy). So the answer is No.',
    """
    Context: "OS, possible peripheral neuropathy but not known nephropathy."
    """.strip(),
    'Answer: The text mentions that the patient has neuropathy. Neuropathy is considered one of the \"major complications\". So the answer is Yes.'
]

example_E = [prompt + 
    """
    Context: "We have reviewed pre procedural expectations and procedural risk including femoral vascular complications, cardiac perforation, renal complications, stroke, heart attack, and death."
    """.strip(),
    "Answer: The text makes no mention of the patient having major diabetes-related complications (Amputation, Kidney damage, Skin conditions, Retinopathy, Nephropathy, and Neuropathy). So the answer is No.",
    """
    Context: "diabetes retinopathy, neuropathy,nephropathy,"
    """.strip(),
    "Answer: The text mentions that the patient has retinopathy, neuropathy, and nephropathy. Retinopathy, neuropathy, and nephropathy are considered \"major complications\" of diabetes. So the answer is Yes.",
    """
    Context: "Renal insufficiency, creatinine 1.6."
    """.strip(),
    'Answer: The text mentions that the patient has renal insufficiency, which is a sign of kidney damage, which is a "major complication" of diabetes. So the answer is Yes.',
    """
    Context: "May need increase in atenolol to bid to avoid plaque rupture in future; now on plavix (gave him some samples b/c of cost), will continue x 6 months; he will avoid exercising for now and discuss cardiac rehab with Dr."
    """.strip(),
    'Answer: The text makes no mention of the patient having major diabetes-related complications (Amputation, Kidney damage, Skin conditions, Retinopathy, Nephropathy, and Neuropathy). So the answer is No.'
]

vicuna_13b_fine_tuned = ["You are a knowledgeable healthcare professional who has been tasked with identifying potential major diabetes-related complications from patient text records. These complications include amputation, kidney damage, skin conditions, retinopathy, nephropathy, neuropathy, and UTI. Please review the patient records provided below and determine if there are any mentions of these major complications. Only answer Yes if there is explicit mention of these major complications for the patient."
]

example_dictionary = {
    "example_A": example_A,
    "example_B": example_B,
    "example_C": example_C,
    "example_D": example_D,
    "example_E": example_E,
    "vicuna_13b_fine_tuned": vicuna_13b_fine_tuned
}