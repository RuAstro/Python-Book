from cProfile import label
import tkinter as tk

window = tk.Tk()


def fahrenheit_to_celsius():
    fahrenheit = entry_temp.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    label_result["text"] = f"{round(celsius, 2)}\N{DEGREE CELSIUS}"


window.title("Temp. Convert")

frame_entry = tk.Frame(master=window)
entry_temp = tk.Entry(master=frame_entry, width=10)
label_temp = tk.Label(master=frame_entry, text="\N{DEGREE FAHRENHEIT}")

entry_temp.grid(row=0, column=0, sticky="E")
label_temp.grid(row=0, column=1, sticky="W")

button_convert = tk.Button(
    master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius
)

label_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

frame_entry.grid(row=0, column=0, padx=10)
button_convert.grid(row=0, column=1, padx=10)
label_result.grid(row=0, column=2, padx=10)

window.mainloop()
