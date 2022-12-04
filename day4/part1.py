INPUT_PATH = "input"

answer = 0

with open(INPUT_PATH) as f:
    pairs = f.read().split('\n')
    for pair in pairs:
        if not pair: continue
        [ elf1, elf2 ] = (list(map(int, elf.split('-'))) for elf in pair.split(','))
        if (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or (elf2[0] >= elf1[0] and elf2[1] <= elf1[1]):
            answer += 1

print(f"Answer: {answer}")