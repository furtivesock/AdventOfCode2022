INPUT_PATH = "input"

inventory_total_calories = []

with open(INPUT_PATH) as f:
    inventories = f.read().split('\n\n')
    for inventory in inventories:
        calories = map(lambda c : int(c) if c else 0, inventory.split('\n'))
        inventory_total_calories.append(sum(calories))

most_calories = max(inventory_total_calories)
print(f"Answer: {most_calories}")

three_most_calories = sum(sorted(inventory_total_calories, reverse=True)[:3])
print(f"Answer: {three_most_calories}")