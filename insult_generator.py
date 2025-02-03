import random

# the first one, saved as a charm

def insult_picker():
    randNumber = random.randint(1, 20)
    dictionaryOfInsults = {
        1 : "scorny, cranially deformed, white, son of a bitch",
        2 : "abysmal fucker",
        3 : "dim-witted, inbred-looking, basement-dwelling goblin",
        4 : "malnourished, off-brand gremlin with the IQ of a potato",
        5 : "sentient disappointment with the charm of a wet sock",
        6 : "deranged, low-effort, bootlegged excuse for a human",
        7 : "underwhelming genetic experiment gone horribly wrong",
        8 : "failed science project with the social skills of a rock",
        9 : "bottom-tier evolutionary mistake, unfit for civilization",
        10 : "atrociously dumb, physically unimpressive amoeba",
        11 : "discount scarecrow with the personality of a moldy sponge",
        12 : "toenail fungus personified into an oxygen thief",
        13 : "radioactive cockroach with the charisma of drywall",
        14 : "malfunctioning AI trapped in an unwashed meat suit",
        15 : "joke of a human, handcrafted by cosmic negligence",
        16 : "half-baked life form with the presence of a tumbleweed",
        17 : "expired bag of mayonnaise masquerading as a person",
        18 : "budget caveman who lost a battle with common sense",
        19 : "embarrassingly primitive, legally questionable organism",
        20 : "walking L with the energy of a deflated bouncy castle"
    }
    return dictionaryOfInsults[randNumber]

# use with something like 
# insult = youABrokeBoy_insult_generator()
# print(f"You're a {insult}")
def youABrokeBoy_insult_generator(): 
    dictionaryOfInsults = {
    1: "broke like a Trotskyist in exile",
    2: "financially starving like a failed five-year plan",
    3: "more overdrawn than a Khrushchev speech",
    4: "penniless like a peasant under war communism",
    5: "still waiting for the revolution like it’s a stimulus check",
    6: "so broke you make the NEP look like a golden age",
    7: "so down bad even Engels wouldn’t sponsor you",
    8: "pockets drier than a Soviet grocery store in ‘91",
    9: "so broke your landlord laughs when you say ‘abolish rent’",
    10: "still tryna collectivize wealth with $2 in your account",
    11: "so poor even Dengist market reforms wouldn’t save you",
    }
    return dictionaryOfInsults[random.randint(1, 11)]

def cranialTheme_insult_generator():
    dictionaryOfInsults = {
    1: "your cranial structure suggests a severe deficiency in strategic foresight",
    2: "the asymmetry of your skull indicates an evolutionary misstep of comical proportions",
    3: "your forehead slope implies a tragic absence of higher reasoning faculties",
    4: "the peculiar flattening of your occipital lobe suggests an ancestral predisposition to running headfirst into walls",
    5: "your skull’s irregular proportions imply a mind burdened by the weight of its own inadequacy",
    6: "the unnatural curvature of your cranium suggests a lifelong struggle with basic arithmetic",
    7: "your cranial ridge is so pronounced it appears to be hoarding unused intelligence",
    8: "judging by your skull shape, your ancestors must have been exceptionally bad at tool use",
    9: "the recession of your frontal lobe suggests a tragic predisposition toward impulsive buffoonery",
    10: "the sheer density of your skull implies an impressive resistance to both logic and common sense",
    11: "the disproportionate width of your skull suggests an unfortunate overinvestment in stubbornness",
    12: "your cranial measurements indicate a mind that is both intellectually barren and deeply confused",
    13: "the peculiar ridges on your skull suggest a history of repeated, and possibly deserved, head trauma",
    14: "your cranium is so underdeveloped it could be mistaken for an evolutionary prototype",
    15: "the depth of your cranial sutures implies an internal struggle between two equally dull halves of a brain",
    16: "your skull’s bizarre topography suggests a deep-rooted aversion to rational thought",
    17: "the excessive thickness of your skull could singlehandedly redefine the limits of human ignorance",
    18: "your cranial proportions indicate an unsettling resistance to learning from past mistakes",
    19: "the unnatural elongation of your skull suggests your thoughts must take the scenic route before reaching any conclusion",
    20: "your skull is shaped in a way that implies your ancestors were allergic to critical thinking"
    }
    return dictionaryOfInsults[random.randint(1, 20)]