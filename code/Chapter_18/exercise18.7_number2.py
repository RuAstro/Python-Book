import tkinter as tk
import random


def click_roll():
    result = random.randint(1, 6)
    label.config(text=f"{result}")


window = tk.Tk()

button = tk.Button(text="Roll", command=click_roll)

label = tk.Label(text="")


button.pack()
label.pack()

window.mainloop()
