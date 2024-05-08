from cProfile import label
import tkinter as tk

# window = tk.Tk()
# # The .pack() Geometry manager
# frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack(fill=tk.Y, side=tk.LEFT)

# frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack(fill=tk.Y, side=tk.LEFT)

# frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
# frame3.pack(fill=tk.Y, side=tk.LEFT)

# window.mainloop()


# The .place() Geometry Manager

window = tk.Tk()

frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="I am at (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=window, text="I am at (75, 75)", bg="yellow")
label2.place(x=75, y=75)

window.mainloop()
