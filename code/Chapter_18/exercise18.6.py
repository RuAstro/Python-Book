import tkinter as tk

window = tk.Tk()

window.title("Address Entry Form")

label1 = tk.Label(text="First Name: ")
entry1 = tk.Entry()

label2 = tk.Label(text="Last Name: ")
entry2 = tk.Entry()

label3 = tk.Label(text="Address Line 1: ")
entry3 = tk.Entry()

label4 = tk.Label(text="Address Line 2: ")
entry4 = tk.Entry()

label5 = tk.Label(text="City: ")
entry5 = tk.Entry()

label6 = tk.Label(text="Province: ")
entry6 = tk.Entry()

label7 = tk.Label(text="Postal Code: ")
entry7 = tk.Entry()

label8 = tk.Label(text="Country : ")
entry8 = tk.Entry()


label1.grid(row=0, column=0, sticky="E")
entry1.grid(row=0, column=1, sticky="W")

label2.grid(row=1, column=0, sticky="E")
entry2.grid(row=1, column=1, sticky="W")

label3.grid(row=2, column=0, sticky="E")
entry3.grid(row=2, column=1, sticky="W")

label4.grid(row=3, column=0, sticky="E")
entry4.grid(row=3, column=1, sticky="W")

label5.grid(row=4, column=0, sticky="E")
entry5.grid(row=4, column=1, sticky="W")

label6.grid(row=5, column=0, sticky="E")
entry6.grid(row=5, column=1, sticky="W")

label7.grid(row=6, column=0, sticky="E")
entry7.grid(row=6, column=1, sticky="W")

label8.grid(row=7, column=0, sticky="E")
entry8.grid(row=7, column=1, sticky="W")


window.mainloop()
