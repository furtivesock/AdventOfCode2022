INPUT_PATH = "input"

PLAYER_SELECTED_POINTS = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

ROUND_POINTS = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3,
}

score = 0

with open(INPUT_PATH) as f:
    rounds = f.read().split('\n')
    for round in rounds:
        if not round:
            continue
        opponent, player = round.split(' ')
        score += PLAYER_SELECTED_POINTS[player] + ROUND_POINTS[opponent + player]

print(f"Answer: {score}")