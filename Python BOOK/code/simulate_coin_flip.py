import random


def coin_flip():
    """Randomly returns 'heads' and 'tails'. """
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"
    
heads_tally = 0
tails_tally = 0

for trail in range(10_000):
    if coin_flip() == "heads":
        heads_tally = heads_tally + 1
        
    else:
        tails_tally = tails_tally + 1
        
ratio = heads_tally / tails_tally
print(f"The ratio of heads to tails is {ratio}")