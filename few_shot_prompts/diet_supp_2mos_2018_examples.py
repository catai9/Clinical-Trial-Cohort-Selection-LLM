prompt = """These are some sentences from a patient's clinical report. Does the text mention that the patient uses a dietary supplement (excluding vitamin D)? Answer Yes or No to the final question. Let's think step by step.""".strip() + "\n\n"

example_A = [prompt + 
    """
    Context: "MEDICATIONS:  Aspirin 81 mg p.o. daily, calcium carbonate 600 mg b.i.d., Diovan 80 mg daily, Glucophage 850 mg b.i.d., lorazepam 1 mg q.i.d. p.r.n., Paxil 10 mg daily, and fluvastatin 20 mg daily, but she ran out some time ago. "
    """.strip(),
    'Answer: The text mentions a prescription of Calcium Carbonate, which is in DIETSUPP. This means that the patient is prescribed a dietary supplement. So the answer is Yes.',
    """
    Context: "ALLERGIES:  Morphine sulfate."
    """.strip(),
    'Answer: The text is about allergies. So the answer is No.',
    '''
    Context: "Chloride (Stat Lab)              103                       (100-108)      mmol/L
    Phosphorus                       3.1                       (2.6-4.5)      mg/dl
    Calcium                          9.7                       (8.5-10.5)     mg/dl"
    '''.strip(),
    'Answer: The text is a physical exam. So the answer is No.',
    '''
    Context: "Mvi (MULTIVITAMINS) 1 CAPSULE PO QD
    Vitamin B12 (CYANOCOBALAMIN) 1000MCG TABLET take 1 Tablet(s) PO QD
    Prilosec OTC (OMEPRAZOLE OTC) 20 MG (20MG TABLET DR take 1) PO QD"
    '''.strip(),
    "Answer: The text mentions a prescription of Multivitamins, which is in DIETSUPP. This means that the patient is prescribed a dietary supplement. So the answer is Yes.",
    '''
    Context: "Physical Exam: Cor S1, S2 normal, no murmurs ."
    '''.strip(),
    "Answer: The text is a physical exam. So the answer is No.",
    '''
    Context: "MEDICATIONS: Lopressor and Zantac as well as Lipitor. ."
    '''.strip(),
    "Answer: The text mentions a prescription of Lopressor, Zantac and Lipitor, which are not dietary supplements. So the answer is No."
]

example_B = [prompt + 
    """
    Context: "Magnesium                1.4                         (1.4-2.0)        meq/L"
    """.strip(),
    'Answer: The text mentions a prescription of Magnesium, which is in DIETSUPP. This means that the patient is prescribed a dietary supplement. So the answer is Yes.',
    """
    Context: "These include atenolol 25, Glucotrol 10 twice a day, Actos 45, Lipitor 40 a day, Lasix 40 a day, and Procardia XL 60 mg q.d., and Coumadin."
    """.strip(),
    "Answer: The text mentions a prescription of atenolol, Glucotrol, Actos, Lipitor, Lasix, Procardia, and Coumadin which are not dietary supplements. So the answer is No.",
    '''
    Context: "6/2128 after similar episodes. The patient has been doing well the cardiologist on call, Dr. sent him to the Emergency Department. All other symptoms are negative as noted in the medical"
    '''.strip(),
    'Answer: The text does not mention any dietary supplements. So the answer is No.',
    '''
    Context: "Lipid/Thyroid Liver and Pancreatic Enzymes"
    '''.strip(),
    'Answer: The text does not mention any dietary supplements. So the answer is No.',
    '''
    Context: "Plasma Potassium                 3.0              L        (3.4-4.8)      mmol/L \nMultivitamin"
    '''.strip(),
    'Answer: The text mentions a prescription of Multivitamins, which is in DIETSUPP. This means that the patient is prescribed a dietary supplement. So the answer is Yes.',
    '''
    Context: "As a result of this, I think it is reasonable for us in addition to having her on atenolol to stop the hydrochlorothiazide, put her on ramipril and a nitrate."
    '''.strip(),
    'Answer: The text does not mention any dietary supplements. So the answer is No.'
]

example_C = [prompt + 
    """
    Context: "Plavix  75mg po daily potassium chloride  10mEq po daily regular insulin  sliding scale sc tid simvastatin  80mg po qpm trazodone  50mg x 1/2 tab po at bedtime vitamin b12  1000 mcg po daily"
    """.strip(),
    'Answer: The text mentions vitamin B12, which is a dietary supplement. This means that the patient is prescribed a dietary supplement. So the answer is Yes.',
    """
    Context: "Cyanocobalamin (Vitamin B12 )  PO 1000 MCG QD"
    """.strip(),
    "Answer: The text mentions a prescription of Cyanocobalamin (Vitamin B12), Ferrous Sulfate, and Coumadin (Warfarin Sodium) which are dietary supplements. So the answer is Yes.",
    '''
    Context: "We will start her on ramipril and long acting nitrate."
    '''.strip(),
    'Answer: The text does not mention any dietary supplements. So the answer is No.',
    '''
    Context: "Nystatin Powder 1 APPLICATION TOP BID; FEN: Low fat, low cholesterol, no concentrated sweets, 2gm sodium, 2L fluid diet"
    '''.strip(),
    'Answer: The text does not mention any dietary supplements. So the answer is No.',
    '''
    Context: "##: Anemia &#8211; iron studies last done in 2116."
    '''.strip(),
    'Answer: The text does not mention any dietary supplements. So the answer is No.',
    '''
    Context: "Mvi (MULTIVITAMINS)   1 TAB PO QD; Caltrate + D (CALCIUM Carbonate 1500 Mg (600 Mg Elem Ca)/ Vit D 200 Iu)   1 TAB PO BID; Colace (DOCUSATE Sodium)   100 MG (100MG TABLET take 1) PO BID x 14 days"
    '''.strip(),
    'Answer: The text mentions a prescription of Mvi (MULTIVITAMINS), Caltrate + D (CALCIUM Carbonate 1500 Mg (600 Mg Elem Ca)/ Vit D 200 Iu), and Colace (DOCUSATE Sodium) which are dietary supplements. So the answer is Yes.'
]

example_D = [prompt + 
    """
    Context: "Toprol XL 50 mg  po daily QTY:30 Start: 12/16/2078"
    """.strip(),
    "Answer: The text does not mention any dietary supplements. So the answer is No.",
    """
    Context: "Calcium 600mg + Vitamin D(400IU) 1 TAB PO tid"
    """.strip(),
    "Answer: The text mentions a prescription of Calcium and Vitamin D, which are dietary supplements. So the answer is Yes.",
    """
    Context: "His current medications include aspirin 81 mg p.o. daily, Axid 150 mg p.o. b.i.d., Cardizem CD 360 mg p.o. daily, Effexor 125 mg p.o. daily, , Lantus 120 units subcutaneously b.i.d., Lasix 60 m p.o. BID nonHD days, lexapro 10 mg p.o. daily, Lipitor 10 mg p.o. daily, cyclosporine 75 mg p.o. b.i.d.,  Toprol-XL 50 mg p.o. daily, vitamin C 500 mg p.o. b.i.d., and vitamin E 400 international units p.o. b.i.d."
    """.strip(),
    'Answer: The text mentions a prescription of vitamin C and vitamin E, which are dietary supplements. So the answer is Yes.',
    """
    Context: "Zocor (SIMVASTATIN) 80 MG (80MG TABLET take 1) PO QHS x 30 days, if you develop muscle pain or weakness, stop the drug immediately and call your doctor."
    """.strip(),
    'Answer: The text does not mention any dietary supplements. So the answer is No.',
    """
    Context: "Tobacco use in the past."
    """.strip(),
    'Answer: The text does not mention any dietary supplements. So the answer is No.',
    """
    Context: "We also treated him with multivitamins."
    """.strip(),
    'Answer: The text mentions the patient has a prescription of multivitamins, which is in DIETSUPP. This means that the patient is prescribed a dietary supplement. So the answer is Yes.'
]

example_E = [prompt + 
    """
    Context: "Magnesium              1.6   1.4-2.0 meq/L      12/13/11 10:40"
    """.strip(),
    "Answer: The text mentions a prescription of Magnesium, which is in DIETSUPP. This means that the patient uses a dietary supplement. So the answer is Yes.",
    """
    Context: "SOCIAL HISTORY:  Smoked in the past for 30 years."
    """.strip(),
    "Answer: The text does not mention any dietary supplements. So the answer is No.",
    """
    Context: "Continue ACE, BUN and Creatine WNL."
    """.strip(),
    'Answer: The text does not mention any dietary supplements. So the answer is No.',
    """
    Context: "samples dispensed of zetia for 6 weeks. will check fasting lipids and ALT. if effective, will contact her insurance for prior authorization"
    """.strip(),
    'Answer: The text does not mention any dietary supplements. So the answer is No.',
    """
    Context: "For now, he is on vitamins and iron supplements as his bowels tolerate."
    """.strip(),
    'Answer: The text mentions the patient is taking vitamins and iron supplements. This means that the patient uses a dietary supplement. So the answer is Yes.',
    """
    Context: "Vitamin B12 (CYANOCOBALAMIN) 250 MCG (250 MCG TABLET Take 1) PO QD #Tablet(s), Mvi (MULTIVITAMINS) 1 TAB PO QD"
    """.strip(),
    'Answer: The text mentions prescriptions of Vitamin B12, and Mvi (Multivitamins). These are dietary supplements. So the answer is Yes.'
]

vicuna_13b_fine_tuned = ["Here is a non-exhaustive list of dietary supplements: DIETSUPP=[{}].".format('AdoMet, Alpha-galactosidase, Amino Acid Powder, Amino Acids, Amino Powder, Amylase, ascorbic acid, B6, BCAA Powder, Bcaas, Beta carotene, Beta-carotene, Bifidobacterium, Biotin, B Vitamins, CaCO3, calcitrate, Calcium, calcium acetate, Calcium Carbonate, Calcium Citrate, Caltrate, Caltrate + D, Caltrate Plus D, Cellulase, Centrum SILVER, chinacea, Chloride, Choline, Chondroitin, Chromium, coconut oil, Cod LIVER OIL, Coenzyme Q10, Copper, CoQ10, Cyanocobalamin, Digestive Enzymes, ephedra, Extracts, Fe Gluconate, Ferrous Gluconate, ferrous sulfate, Fish oil, flaxseed, flaxseed oil, folate, Folic acid, garlic, ginger, ginkgo, ginseng, Glucoamylase, Glucosamine, green tea, GTE, Hemicellulase, herbal extracts, Herbs, herbs extracts, Inositol, Invertase, Iodine, iron, kava, KCl, Klor-con, Lactase, Lactobacillus, lecithin, Lipase, magnesium, Magnesium Gluconate, magnesium oxide, Manganese, Melatonin, Menopause, mineral, Molybdenum, multivitamins, MVI, Mvi ELIXIR, Nephrocaps, NEPHRO-VIT RX, Niacin, Niferex, Nutrition Bars, Nutrition Drinks, Ocuvite, omega-3, OMEGA-3-FATTY ACIDS, Omega-3s, Oscal+d, PABA, Pantothenic acid, Para-aminobenzoic acid, Pectinase, Peptidase, PhosLo, Phos Lo, Phosphorus, Phytase, Plant Sterols, potassium, potassium chloride, Potassium supplementation, Powders, Probiotics, Protease, PYRIDOXINE, red yeast rice, resveratrol, retinol, Riboflavin, S-adenosyl-L-methionine, SAMe, saw palmetto, Selenium, Sexual Enhancement Supplements, Shakes, sodium bicarbonate, Sports Supplements, stanol, sterol, St John’s wort, Super Fruits, Thiamin, TOCOPHEROL-DL-ALPHA, Tums, valerian, Vitamin A, Vitamin A-1, Vitamin B1, vitamin b12, Vitamin B-12, Vitamin B2, vitamin B3, Vitamin B5, Vitamin B 6, Vitamin B-6, Vitamin B7, Vitamin B9, vitamin C, vitamin E, Vitamin K, Vit B12, vit C, Xylanase, zinc') + "\n\n" + """
            Now, these are some sentences from a patient's clinical report. Does the patient use a dietary supplement from DIETSUPP? Let's think step by step.
            """.strip()  + "\n\n" + """
    Context: "MEDICATIONS:  Aspirin 81 mg p.o. daily, calcium carbonate 600 mg b.i.d., Diovan 80 mg daily, Glucophage 850 mg b.i.d., lorazepam 1 mg q.i.d. p.r.n., Paxil 10 mg daily, and fluvastatin 20 mg daily, but she ran out some time ago. "
    """.strip(),
    'Answer: The text mentions a prescription of Calcium Carbonate, which is in DIETSUPP. This means that the patient is prescribed a dietary supplement. So the answer is Yes.',
    """
    Context: "ALLERGIES:  Morphine sulfate."
    """.strip(),
    'Answer: The text is about allergies. So the answer is No.',
    '''
    Context: "Chloride (Stat Lab)              103                       (100-108)      mmol/L
    Phosphorus                       3.1                       (2.6-4.5)      mg/dl
    Calcium                          9.7                       (8.5-10.5)     mg/dl"
    '''.strip(),
    'Answer: The text is a physical exam. So the answer is No.',
    '''
    Context: "Mvi (MULTIVITAMINS) 1 CAPSULE PO QD
    Vitamin B12 (CYANOCOBALAMIN) 1000MCG TABLET take 1 Tablet(s) PO QD
    Prilosec OTC (OMEPRAZOLE OTC) 20 MG (20MG TABLET DR take 1) PO QD"
    '''.strip(),
    "Answer: The text mentions a prescription of Multivitamins, which is in DIETSUPP. This means that the patient is prescribed a dietary supplement. So the answer is Yes.",
    '''
    Context: "Physical Exam: Cor S1, S2 normal, no murmurs ."
    '''.strip(),
    "Answer: The text is a physical exam. So the answer is No.",
    '''
    Context: "MEDICATIONS: Lopressor and Zantac as well as Lipitor. ."
    '''.strip(),
    "Answer: The text mentions a prescription of Lopressor, Zantac and Lipitor, which are not dietary supplements. So the answer is No."
]

example_dictionary = {
    "example_A": example_A,
    "example_B": example_B,
    "example_C": example_C,
    "example_D": example_D,
    "example_E": example_E,
    "vicuna_13b_fine_tuned": vicuna_13b_fine_tuned
}