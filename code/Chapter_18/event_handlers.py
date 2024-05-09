import tkinter as tk

window = tk.Tk()

events_list = []


def handle_keypress(event):
    print(event.char)


while True:
    if events_list == []:
        continue
    event = events_list[0]

    if event.type == "keypress":
        handle_keypress(event)

    window.mainloop()
