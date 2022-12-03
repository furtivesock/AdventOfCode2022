INPUT_PATH = "input"

answer = 0

with open(INPUT_PATH) as f:
    rucksacks = f.read().split('\n')
    for i in range(0, len(rucksacks), 3):
        for item in rucksacks[i]:
            if item in rucksacks[i + 1] and item in rucksacks[i + 2]:
                answer += ord(item) - 96 if ord(item) >= 97 else ord(item) - 38
                break

print(f"Answer: {answer}")