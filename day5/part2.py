import re

INPUT_PATH = "input"
STACKS_COUNT = 9

answer = 0
stacks = [ [] for _ in range(STACKS_COUNT) ]
moves = []

input = open(INPUT_PATH)
content = input.readlines()

for i in reversed(range(8)):
    crates = []
    for j in range(1, len(content[7]), 4):
        crates.append(content[i][j] if content[i][j] != ' ' else None)
    for j in range(STACKS_COUNT):
        if crates[j] is None:
            continue
        stacks[j].append(crates[j])

instructions = content[10:]

for instruction in instructions:
    if not instruction:
        continue
    count, src, dest = list(map(int, re.search(r'move (\d+) from (\d) to (\d)', instruction).groups()))
    crates = stacks[src - 1][len(stacks[src - 1]) - count:]
    del stacks[src - 1][len(stacks[src - 1]) - count:]
    stacks[dest - 1].extend(crates)

answer = ''.join([ stack[-1] for stack in stacks ])
print(f"Answer: {answer}")