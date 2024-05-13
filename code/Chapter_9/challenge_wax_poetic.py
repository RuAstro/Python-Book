import random
random.seed(input("Give a seed: "))
noun = [
    "fossil",
    "horse",
    "aardvark",
    "judge",
    "chef",
    "mango",
    "extrovert",
    "gorilla"
]

verbs = [
    "kicks",
    "jingles",
    "bounces",
    "slurps",
    "meows",
    "explodes",
    "curdles"
]

adjectives = [
    "furry",
    "balding",
    "incredulous",
    "fragrant",
    "exuberant",
    "glistening"
]

prepositions = [
    "against",
    "after",
    "into",
    "beneath",
    "upon",
    "for",
    "in",
    "like",
    "over",
    "within"
]

adverbs = [
    "curiously",
    "extravagantly",
    "tantalizingly",
    "furiously",
    "sensuously"
]

def make_poem():
    """Create randomly generated poem, returned as a multi-line string."""
    
    n1 = random.choice(noun)
    n2 = random.choice(noun)
    n3 = random.choice(noun)
    
    while n1 == n2:
        n2 = random.choice(noun)
    while n1 == n3 or n2 == n3:
        n3 = random.choice(noun)
       
        
    v1 = random.choice(verbs)
    v2 = random.choice(verbs)
    v3 = random.choice(verbs)
    
    while v1 == v2:
        v2 = random.choice(verbs)
    while v1 == v3 or v2 == v3:
        v3 = random.choice(verbs)
        
    
    adj1 = random.choice(adjectives)
    adj2 = random.choice(adjectives)
    adj3 = random.choice(adjectives)
    while adj1 == adj2:
        adj2 = random.choice(adjectives)
    while adj1 == adj3 or adj2 == adj3:
        adj3 = random.choice(adjectives)
        
        
    prep1 = random.choice(prepositions)
    prep2 = random.choice(prepositions)
    while prep1 == prep2:
        prep2 = random.choice(prepositions)
    
    
    adv1 = random.choice(adverbs)
    
    if "aeiou".find(adj1[0]) != -1:
        article = "An"
    else:
        article = "A"
        
        
    poem = (
        f"{article} {adj1} {n1}\n\n"
        f"{article} {adj1} {n1} {v1} {adj2} {n2}\n"
        f"{adv1}, the {n1} {v2}\n"
        f"the {n2} {v3} {prep2} a {adj3} {n3}"
    )
    
    
    return poem

poem = make_poem()
print(poem)