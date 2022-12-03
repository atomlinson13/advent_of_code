from aocd.models import Puzzle, User

WIN_POINTS = 6
DRAW_POINTS = 3
LOSE_POINTS = 0

game_options = {
    "X": 1,  # rock
    "Y": 2,  # paper
    "Z": 3  # scissors
}

winning_combo = ["C X", "A Y", "B Z"]
losing_combo = ["A Z", "B X", "C Y"]
draw_combo = ["A X", "B Y", "C Z"]


def part_1(data):
    total = 0
    for i in data:
        my_play = i[-1]
        if i in winning_combo:
            total += (WIN_POINTS + game_options[my_play])
        elif i in draw_combo:
            total += (DRAW_POINTS + game_options[my_play])
        else:
            total += (LOSE_POINTS + game_options[my_play])

    return total


def part_2(data):
    game_outcome = {
        "X": {"points": LOSE_POINTS, "combo": losing_combo},
        "Y": {"points": DRAW_POINTS, "combo": draw_combo},
        "Z": {"points": WIN_POINTS, "combo": winning_combo}
    }

    total = 0
    for i in data:
        opponent_play = i[0]
        outcome = i[-1]

        must_play = next(filter(lambda x: opponent_play in x, game_outcome[outcome]["combo"]))[-1]

        total += game_outcome[outcome]["points"] + game_options[must_play]

    return total


user = User(token="")
puzzle = Puzzle(year=2022, day=2, user=user)
input_data = puzzle.input_data.splitlines()

puzzle.answer_a = part_1(input_data)
puzzle.answer_b = part_2(input_data)
puzzle.solve()
