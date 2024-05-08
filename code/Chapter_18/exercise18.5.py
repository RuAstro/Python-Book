import tkinter as tk

# border_effects = {"Bingo": tk.RAISED}

# window = tk.Tk()

# for relief_name, relief in border_effects.items():

#     frame = tk.Frame(master=window, relief=relief, borderwidth=5)

#     frame.pack(side=tk.LEFT)

#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()

#     window.mainloop()


# Exercise 2
# window = tk.Tk()

# button = tk.Button(
#     window, text="Click Here", bg="white", fg="blue", width=50, height=25
# )
# button.pack()
# window.mainloop()


# Exercise 3
window = tk.Tk()

entry = tk.Entry(window, bg="white", fg="black", width=40)

entry.insert(0, "What is your name? ")
entry.pack()

window.mainloop()
