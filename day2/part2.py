INPUT_PATH = "input"

DRAW_POINTS = 3
WIN_POINTS = 6

ROCK_POINTS = 1
PAPER_POINTS = 2
SCISSOR_POINTS = 3

STRATEGIES = {
    # Lose
    "X": {
        "A": SCISSOR_POINTS,
        "B": ROCK_POINTS,
        "C": PAPER_POINTS
    },
    # Draw
    "Y": {
        "A": ROCK_POINTS + DRAW_POINTS,
        "B": PAPER_POINTS + DRAW_POINTS,
        "C": SCISSOR_POINTS + DRAW_POINTS
    },
    # Win
    "Z": {
        "A": PAPER_POINTS + WIN_POINTS,
        "B": SCISSOR_POINTS + WIN_POINTS,
        "C": ROCK_POINTS + WIN_POINTS
    }
}

score = 0

with open(INPUT_PATH) as f:
    rounds = f.read().split('\n')
    for round in rounds:
        if not round:
            continue
        opponent, strategy = round.split(' ')
        score += STRATEGIES[strategy][opponent]

print(f"Answer: {score}")