import easygui as gui

path = gui.fileopenbox(title="Select a file")

if path is None:
    exit()
