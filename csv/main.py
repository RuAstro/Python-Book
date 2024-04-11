from pathlib import Path
import csv

#path to the high_scores.csv file
high_scores = set()
#the path to the scores.csv file
scores_files = Path("scores.csv")
#initialize a set to store unique player names
names = set()
scores = []
#initialize a dictionary to store each players highest score
player_scores = {}

#find highest score for each player
with scores_files.open(mode = "r", encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["name"]
        score = int(row["score"])
        
        #add players names to set of names
        names.add(name)
        
        #when update needed
        if name in player_scores:
            player_scores[name] = max(player_scores[name], score)
        else:
            player_scores[name] = score
            

with high_scores.open(mode = "w", encoding = "utf-8", newline = "") as file:
    writer = csv.writer(file)
    for name in names:
        writer([name, player_scores[name]])
            
print(scores_files(row))
print("High scores saved to file")






    
#     next(file)
#     for line in file:
#         name, score = line.split(',')
#         names.add(name)
#         scores.append(int(score.strip()))
#         high_scores.add(name)
#         high_scores[name].append(int(score.strip()))

# print(names)
# print(scores)
# print(high_scores)

# {red: [1, 69, 42, 55]}