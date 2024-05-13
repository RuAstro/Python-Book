import tkinter as tk
import random
from tkinter import filedialog


def generate_poetry():
    nouns = nouns_entry.get().split()
    verbs = verbs_entry.get().split()
    adjectives = adjectives_entry.get().split()
    prepositions = prepositions_entry.get().split()
    adverbs = adverbs_entry.get().split()

    if (
        len(nouns) < 3
        or len(verbs) < 3
        or len(adjectives) < 3
        or len(prepositions) < 3
        or len(adverbs) < 1
    ):
        poetry_text.delete(1.0, tk.END)
        poetry_text.insert(tk.END, "Error: Not enough words entered.")
    else:
        poem = generate_poem(nouns, verbs, adjectives, prepositions, adverbs)
        poetry_text.delete(1.0, tk.END)
        poetry_text.insert(tk.END, poem)


def generate_poem(nouns, verbs, adjectives, prepositions, adverbs):
    adjective1, adjective2, adjective3 = random.sample(adjectives, 3)
    noun1, noun2, noun3 = random.sample(nouns, 3)
    verb1, verb2, verb3 = random.sample(verbs, 3)
    prepositions1, prepositions2, prepositions3 = random.sample(prepositions, 3)
    adverb = random.choice(adverbs)

    poem = (
        f"A {adjective1} {noun1}\n"
        f"{adjective1} {noun1} {verb1} {prepositions1} the {adjective2} {noun2}\n"
        f"{adverb}, the {noun1} {verb2}\n"
        f"the {noun2} {verb3} {prepositions2} a {adjective3} {noun3}"
    )
    return poem.capitalize()


def export_poem():
    poem_content = poetry_text.get(1.0, tk.END)
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(poem_content)


window = tk.Tk()
window.title("Poem Generator")

nouns_label = tk.Label(window, text="Nouns:")
nouns_label.grid(row=0, column=0, sticky="E")
nouns_entry = tk.Entry(window)
nouns_entry.grid(row=0, column=1)

verbs_label = tk.Label(window, text="Verbs:")
verbs_label.grid(row=1, column=0, sticky="E")
verbs_entry = tk.Entry(window)
verbs_entry.grid(row=1, column=1)

adjectives_label = tk.Label(window, text="Adjectives:")
adjectives_label.grid(row=2, column=0, sticky="E")
adjectives_entry = tk.Entry(window)
adjectives_entry.grid(row=2, column=1)

prepositions_label = tk.Label(window, text="Prepositions:")
prepositions_label.grid(row=3, column=0, sticky="E")
prepositions_entry = tk.Entry(window)
prepositions_entry.grid(row=3, column=1)

adverbs_label = tk.Label(window, text="Adverbs:")
adverbs_label.grid(row=4, column=0, sticky="E")
adverbs_entry = tk.Entry(window)
adverbs_entry.grid(row=4, column=1)

generate_button = tk.Button(window, text="Generate Poetry", command=generate_poetry)
generate_button.grid(row=5, column=1)

export_button = tk.Button(window, text="Export to file", command=export_poem)
export_button.grid(row=5, column=2)

poetry_label = tk.Label(window, text="Generated Poem:")
poetry_label.grid(row=6, column=0, sticky="E")

poetry_text = tk.Text(window, width=40, height=10)
poetry_text.grid(
    row=7, column=0, columnspan=10
)  # The columnspan attribute in Tkinter specifies how many columns a widget should span. It's used when you want a widget to cover multiple columns in a grid layout.

window.mainloop()
