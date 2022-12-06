INPUT_PATH = "input"
SIZE = 14 # 4 for part 1

content = open(INPUT_PATH).readlines()[0]
answer = None

for i in range(len(content)):
    if len(set(content[i:i + SIZE])) == SIZE:
        answer = i + SIZE
        break

print(f"Answer: {answer}")