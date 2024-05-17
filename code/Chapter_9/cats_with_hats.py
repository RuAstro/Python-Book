cats = [False] * 100  # Initially, no cat has a hat

# Iterate through each round
for round_number in range(1, 101):
    # Iterate through each cat
    for cat_number in range(round_number - 1, 100, round_number):
        # Toggle the hat
        cats[cat_number] = not cats[cat_number]

# Print out the cats that have hats
for i, has_hat in enumerate(cats, start=1):
    if has_hat:
        print("Cat", i, "has a hat.")
