import easygui as gui

gui.msgbox(msg="Hello!", title="My first message box", ok_button="Click me")

gui.buttonbox(
    msg="What is your fav color?",
    title="Choose wisely...",
    choices=("Red", "Yellow", "Blue"),
)


gui.indexbox(
    msg="What is your fav color?",
    title="Choose wisely...",
    choices=("Red", "Yellow", "Blue"),
)

gui.enterbox(
    msg="What is your fav color?",
    title="Choose wisely...",
)

gui.fileopenbox(title="Select a file")
