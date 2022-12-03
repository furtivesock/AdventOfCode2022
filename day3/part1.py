INPUT_PATH = "input"

answer = 0

with open(INPUT_PATH) as f:
    rucksacks = f.read().split('\n')
    for rucksack in rucksacks:
        comp_size = len(rucksack) // 2
        comp1, comp2 = rucksack[:comp_size], rucksack[comp_size:]
        for item in comp1:
            if item in comp2:
                answer += ord(item) - 96 if ord(item) >= 97 else ord(item) - 38
                break

print(f"Answer: {answer}")