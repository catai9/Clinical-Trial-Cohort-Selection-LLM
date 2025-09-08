prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient uses aspirin to prevent myocardial infarction (MI)? Answer Yes or No to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "MEDICATIONS:  Aspirin 81 mg p.o. daily, calcium carbonate 600 mg b.i.d., Diovan 80 mg daily, Glucophage 850 mg b.i.d., lorazepam 1 mg q.i.d. p.r.n., Paxil 10 mg daily, and fluvastatin 20 mg daily, but she ran out some time ago."
    """.strip(),
    'Answer: The text mentions a prescription of aspirin with a dose of 81 mg daily. 81 mg is a low dose (less than 325 mg). So the answer is Yes.',
    """
    Context: "MEDICATIONS: Synthroid, Hydralazine, Lopressor, prednisone, Coumadin,"
    """.strip(),
    'Answer: The text mentions several medications, but does not mention aspirin. So the answer is No.',
    """
    Context: "EMS gave her 3 puffs of NTG and 4 baby ASA w/o effect. "
    """.strip(),
    'Answer: The text mentions a prescription of baby aspirin (ASA). Baby aspirin is a common name for low-dose aspirin. So the answer is Yes.',
    """
    Context: "1. Aspirin."
    """.strip(),
    'Answer: The text mentions a prescription of aspirin, but does not mention the dose. So the answer is No.',
    """
    Context: "Ecotrin 325 mg PO QD"
    """.strip(),
    'Answer: The text mentions a prescription of aspirin (Ecotrin) with a dose of 325 mg daily (QD). 325 mg is a low dose (less than 325 mg). So the answer is Yes.',
    '''
    Context: "ALLERGIES:  She has an allergy to codeine, aspirin, erythromycin,"
    '''.strip(),
    "Answer: The text mentions an allergy to aspirin. So the answer is No."
]

example_B = [prompt + 
    """
    Context: "ASPIRIN   325MG PO QD COUMADIN (WARFARIN SODIUM) 2.5MG 1 Tablet(s) PO QPM CLOPIDOGREL"
    """.strip(),
    'Answer: The text mentions a prescription of aspirin (Ecotrin) with a dose of 325 mg daily (QD). 325 mg is a low dose (less than 325 mg). So the answer is Yes.',
    """
    Context: "ASA 325 mg  po qd In the ED, patient was treated with ASA, metoprolol, sl NTG, and chest pain resolved."
    """.strip(),
    'Answer: The text mentions a prescription of aspirin (Ecotrin) with a dose of 325 mg daily (QD). 325 mg is a low dose (less than 325 mg). So the answer is Yes.',
    """
    Context: "Aspirin - ulcer, : Allergy entered as ASA Lisinopril 40 MG (40MG TABLET take 1) PO QD"
    """.strip(),
    'Answer: The text mentions a prescription of aspirin, but states that it is used to treat allergy. The aspirin is not used to prevent MI. So the answer is No.',
    """
    Context: "Low dose aspirin therapy could also be considered. Her only medication is lente insulin taken twice per day. Prilosec, Ultram, verapamil, PhosLo, Coumadin, Renax, Colace, and MEDICATIONS:  The patient takes methylphenidate, Ambien, Medications: See previous notes."
    """.strip(),
    'Answer: The text mentions a prescription of aspirin, but does not mention the dose. So the answer is No.',
    """
    Context: "aspirin  81 mg po daily"
    """.strip(),
    'Answer: The text mentions a prescription of aspirin with a dose of 81 mg daily. 81 mg is a low dose (less than 325 mg). So the answer is Yes.',
    '''
    Context: "he remains on a plethora of medications including NPH insulin 64
    units sub q qAM along with 34 units CZI sub q qAM and 68 units NPH
    sub q qPM, enteric coated aspirin one tab po q.d., Captopril 25 mg
    po t.i.d., Lasix 40 mg po b.i.d."
    '''.strip(),
    "Answer: The text mentions a prescription of aspirin with a dose of one tab daily. This is not a low dose. So the answer is No."
]

example_C = [prompt + 
    """
    Context: "ASA (ACETYLSALICYLIC ACID)   81MG 1 Tablet(s) PO QD"
    """.strip(),
    'Answer: The text mentions a prescription of aspirin (Ecotrin) with a dose of 81 mg daily (QD). 81 mg is a low dose (less than 81 mg). So the answer is Yes.',
    """
    Context: "Pt received ASA 325 and lasix 40 mg IV, and was sent to WGH ED."
    """.strip(),
    'Answer: The text mentions a prescription of aspirin (Ecotrin) with a dose of 325 mg (ASA). So the answer is Yes.',
    """
    Context: "Aspirin:  avoid for 7 days before surgery. -no antiplatelet or anticoagulation for now; Diabetes mellitus Type II - On Humulin 15/15"
    """.strip(),
    'Answer: The text mentions a prescription of aspirin, but states that it should be avoided for 7 days before surgery. The aspirin is not used to prevent MI. So the answer is No.',
    """
    Context: "ASA qd for now.  follow up with neurology as scheduled on 9/02/16."
    """.strip(),
    'Answer: The text mentions a prescription of aspirin, but does not mention the dose. So the answer is No.',
    """
    Context: "Meds:  Procardia XL 120 mg. q.d.  Aspirin 325 mg. q.d.  Lopressor 100 mg. b.i.d.  Micronase 5 mg. q.d."
    """.strip(),
    'Answer: The text mentions a prescription of aspirin with a dose of 325 mg daily. 325 mg is a low dose. So the answer is Yes.',
    """
    Context: "IBUPROFEN 800 MG (800MG TABLET take 1) PO TID PRN pain x 30 days, Take with food or milk."
    """.strip(),
    'Answer: The text mentions a prescription of aspirin (Ecotrin) with a dose of 800 mg (TID). 800 mg is a high dose (more than 325 mg). So the answer is No.'
]

example_D = [prompt + 
    """
    Context: "ASA 81mg  po daily Start: 12/16/2134; He will continue the medical regimen of ASA 81mg daily, Lipitor 20mg daily, Toprol XL 25mg daily and Lisinopril 10mg daily."
    """.strip(),
    "Answer: The text mentions a prescription of aspirin (Ecotrin) with a dose of 81 mg daily (PO). 81 mg is a low dose (less than 325 mg). So the answer is Yes.",
    """
    Context: "Aspirin:  avoid for 7 days before surgery"
    """.strip(),
    "Answer: The text mentions a prescription of aspirin, but does not mention the dose. The text also mentions that the patient should avoid aspirin for 7 days before surgery. So the answer is No.",
    """
    Context: "Current Medications:  Calcium with D 1250 mg twice per day, Cardura 4 mg, CellCept 1000 mg twice per day, diltiazem CD 240 mg twice per day, Ecotrin 81 mg per day, Lantus insulin 26 units at night, magnesium oxide 400 mg twice per day, vitamin, cyclosporine 100 mg twice per day, Neurontin 100 mg twice per day, NovoLog insulin as needed, prednisone 5 mg per day, vitamins C 500 mg twice per day, and vitamin E 400 units twice per day."
    """.strip(),
    'Answer: The text mentions a prescription of aspirin (Ecotrin) with a dose of 325 mg daily (QD). 325 mg is a low dose (less than 325 mg). So the answer is Yes.',
    """
    Context: "Omeprazole 20 MG (20MG CAPSULE DR take 1) PO QD"
    """.strip(),
    'Answer: The text does not mention anything about aspirin. So the answer is No.',
    """
    Context: "Since then, he has been doing well and has been instructed to be on double dose clopidogrel 150 mg lifelong and full dose aspirin 325 mg p.o. daily lifelong."
    """.strip(),
    'Answer: The text mentions a prescription of aspirin with a dose of 325 mg daily. 325 mg is a low dose. So the answer is Yes.',
    """
    Context: "THERAPY RENDERED/COURSE IN ED:  The patient was treated in the emergency department with O2, two liters via nasal cannula, nitroglycerin 1/150 sublingual times three, Lopressor 25 mg p.o., and aspirin 325 mg p.o.  The patient became pain-free and remained  hemodynamically stable."
    """.strip(),
    'Answer: The text mentions a prescription of aspirin with a dose of 325 mg. 325 mg is a low dose. So the answer is Yes.'
]

example_E = [prompt + 
    """
    Context: "ASA Physical Status III-patients will see Dr.; clopidogrel, ASA. ASA 325"
    """.strip(),
    "Answer: The text mentions a prescription of aspirin (Ecotrin) with a dose of 325 mg daily (QD). 325 mg is a low dose. So the answer is Yes.",
    """
    Context: "---continue ASA 81mg qd"
    """.strip(),
    "Answer: The text mentions a prescription of aspirin (Ecotrin) with a dose of 81 mg daily (QD). 81 mg is a low dose (less than 325 mg). So the answer is Yes.",
    """
    Context: "Aspirin causes rash. ALLERGIES:  She has an allergy to codeine, aspirin, erythromycin,"
    """.strip(),
    'Answer: The text mentions a prescription of aspirin, but states that it causes rash. The aspirin is not used to prevent MI. So the answer is No.',
    """
    Context: "THERAPY RENDERED/COURSE IN ED:  Aspirin was given and she is chest"
    """.strip(),
    'Answer: The text mentions a prescription of aspirin, but does not mention the dose. So the answer is No.',
    """
    Context: "He is now carefully using ibuprofen and has follow up scheduled with"
    """.strip(),
    'Answer: The text mentions a prescription of ibuprofen, but does not mention aspirin. So the answer is No.',
    """
    Context: "The patient is currently on no hypolipemic medication. Prescriptions for nifedipine and the clonidine patch were refilled."
    """.strip(),
    'Answer: The text does not mention anything about aspirin. So the answer is No.'
]

vicuna_13b_fine_tuned = [
    "Here are a few ways of naming aspirin: {}.".format('aspirin, ASA, activase, aspir, Ascriptin, Aspergum, Aspirtab, Easprin, Ecotrin, Ecpirin, Fasprin, Halfprin, Miniprin, Ecpirin, Entercote, Genacote, Ninoprin, Norwich, Bufferin Low Dose, acetyl salicylic') + "\n\n" + """
    Now, these are some sentences from a patient's clinical report. Has the patient been prescribed low dose aspirin? A low-dose aspirin is a dose of 325 mg or lower. Let's think step by step.
    """.strip()  + "\n\n" + 
    """
    Context: "MEDICATIONS:  Aspirin 81 mg p.o. daily, calcium carbonate 600 mg b.i.d., Diovan 80 mg daily, Glucophage 850 mg b.i.d., lorazepam 1 mg q.i.d. p.r.n., Paxil 10 mg daily, and fluvastatin 20 mg daily, but she ran out some time ago."
    """.strip(),
    'Answer: The text mentions a prescription of aspirin with a dose of 81 mg daily. 81 mg is a low dose (less than 325 mg). So the answer is Yes.',
    """
    Context: "MEDICATIONS: Synthroid, Hydralazine, Lopressor, prednisone, Coumadin,"
    """.strip(),
    'Answer: The text mentions several medications, but does not mention aspirin. So the answer is No.',
    """
    Context: "EMS gave her 3 puffs of NTG and 4 baby ASA w/o effect. "
    """.strip(),
    'Answer: The text mentions a prescription of baby aspirin (ASA). Baby aspirin is a common name for low-dose aspirin. So the answer is Yes.',
    """
    Context: "1. Aspirin."
    """.strip(),
    'Answer: The text mentions a prescription of aspirin, but does not mention the dose. So the answer is No.',
    """
    Context: "Ecotrin 325 mg PO QD"
    """.strip(),
    'Answer: The text mentions a prescription of aspirin (Ecotrin) with a dose of 325 mg daily (QD). 325 mg is a low dose (less than 325 mg). So the answer is Yes.',
    '''
    Context: "ALLERGIES:  She has an allergy to codeine, aspirin, erythromycin,"
    '''.strip(),
    "Answer: The text mentions an allergy to aspirin. So the answer is No.",
    '''
    Context: "The remains on a plethora of medications including NPH insulin 64 units sub q qAM along with 34 units CZI sub q qAM and 68 units NPH sub q qPM, enteric coated aspirin one tab po q.d., Captopril 25 mg po t.i.d., Lasix 40 mg po b.i.d."
    '''.strip(),
    "Answer: The text mentions a prescription of aspirin with a dose of one tab daily. This is not a low dose. So the answer is No."
]

example_dictionary = {
    "example_A": example_A,
    "example_B": example_B,
    "example_C": example_C,
    "example_D": example_D,
    "example_E": example_E,
    "vicuna_13b_fine_tuned": vicuna_13b_fine_tuned
}