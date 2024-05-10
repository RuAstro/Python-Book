import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfile


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor - {filepath}")


def save_file():
    filepath = asksaveasfile(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )

    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor - {filepath}")


window = tk.Tk()
window.title("Text Editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

button_open = tk.Button(fr_buttons, text="Open", command=open_file)
button_save = tk.Button(fr_buttons, text="Save as...", command=save_file)

button_open.grid(row=0, column=0, sticky="EW", padx=5, pady=5)
button_save.grid(row=0, column=1, sticky="EW", padx=5)


txt_edit.grid(row=0, column=1, sticky="nsew")
fr_buttons.grid(row=0, column=0, sticky="NS")


window.mainloop()
