from random import random

num_times_A_wins = 0
num_times_B_wins = 0

num_trails = 10_000
for trail in range(0, num_trails):
    votes_for_A = 0
    votes_for_B = 0
   #First regions 
if random() < 0.87:
    votes_for_A = votes_for_A + 1
else:
    votes_for_B = votes_for_B + 1
    #Second regions 
if random() < 0.65:
    votes_for_A = votes_for_A + 1
else:
    votes_for_B = votes_for_B + 1
    #Third regions 
if random() < 0.17:
    votes_for_A = votes_for_A + 1
else:
    votes_for_B = votes_for_B + 1
    

#outcome...
if votes_for_A > votes_for_B:
    num_times_A_wins = num_times_A_wins + 1
    
else:
    num_times_B_wins = num_times_B_wins + 1
    
    
print(f"Probability A wins: {num_times_A_wins / num_trails}")
print(f"Probability B wins: {num_times_B_wins / num_trails}")    