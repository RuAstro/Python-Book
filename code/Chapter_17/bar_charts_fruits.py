from matplotlib import pyplot as plt

fruits = {"apples": 10, "oranges": 16, "bananas": 9, "pears": 4}

plt.bar(fruits.keys(), fruits.values())
plt.show()
