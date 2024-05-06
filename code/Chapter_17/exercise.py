from matplotlib import pyplot as plt
import csv
import os

# import pandas as pd

pirates = []
temp = []

with open("code/Chapter_17/pirates.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        pirates.append(int(row["Number of Pirates"]))
        temp.append(float(row["Global Temp."]))

# data = pd.read_csv("pirates.csv")

# pirates = data["number of pirates"]
# temp = data["Global temp"]

plt.plot(pirates, temp, marker="o", linestyle="-")

plt.xlabel("number of pirates")
plt.ylabel("global temp")
plt.title("Do pirates cause global warming?")

plt.savefig("pirates_global_warming.png")

plt.show()
