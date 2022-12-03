from aocd.models import Puzzle, User


def part_1(data):
    largest_sum = 0
    current_sum = 0
    for d in data:
        if d == "":
            if current_sum > largest_sum:
                largest_sum = current_sum
            current_sum = 0
        else:
            current_sum += int(d)
    return largest_sum


def part_2(data):
    calories = []
    current_sum = 0
    for d in data:
        if d == "":
            calories.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(d)

    calories.sort()

    return sum(calories[-3:])


user = User(token="")
puzzle = Puzzle(year=2022, day=1, user=user)
input_data = puzzle.input_data.splitlines()

puzzle.answer_a = part_1(input_data)
puzzle.answer_b = part_2(input_data)
puzzle.solve()