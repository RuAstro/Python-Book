import tkinter as tk
import random


def generate_poetry():
    nouns = nouns_entry.get().split()
    verbs = verbs_entry.get().split()
    adjectives = adjectives_entry.get().split()
    prepositions = prepositions_entry.get().split()
    adverbs = adverbs_entry.get().split()
    adverb = random.choice(adverbs_user) if adverbs_user else ""

    if (
        len(nouns) < 3
        or len(verbs) < 3
        or len(adjectives) < 3
        or len(prepositions) < 3
        or len(adverbs) < 1
    ):
        poetry_text.delete()
        poetry_text.insert()
    else:
        poem = generate_poem(nouns, verbs, adjectives, prepositions, adverbs)
        poetry_text.delete()
        poetry_text.insert()


def generate_poem(nouns, verbs, adjectives, prepositions, adverbs):
    poem = ""
    for _ in range(4):
        line = f"{random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(prepositions)} {random.choice(adverbs)}."
        poem += line.capitalize() + "\n"
    return poem


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
generate_button.grid(row=5, column=2)

poetry_label = tk.Label(window, text="Generated Poem:")
poetry_label.grid(row=6, column=2)

poetry_text = tk.Text(window, width=40, height=10)
poetry_text.grid(row=7, column=2)

window.mainloop()
