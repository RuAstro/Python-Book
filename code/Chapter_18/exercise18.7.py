import tkinter as tk
import random


def change_color():
    colors = ["red", "orange", "yellow", "blue", "green", "indigo", "violet"]
    button.config(bg=random.choice(colors))


window = tk.Tk()
window.title("Button Color Change")

button = tk.Button(text="Click me", fg="black", command=change_color)


button.pack()
window.mainloop()
