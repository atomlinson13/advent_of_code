from aocd.models import Puzzle, User


def part_1(data):
    letters = []
    for line in data:
        line = list(line)
        length = int(len(line) / 2)
        l1 = line[:length]
        l2 = line[length:len(line)]

        for s in l1:
            if s in l2:
                letters.append(s)
                break
    total = 0
    for l in letters:
        num = (ord(l) - 96)
        if num <= 0:
            num = (ord(l.lower()) - 96) + 26
        total += num

    return total


def part_2(data):
    total = 0
    letters = []

    for line in range(0, len(data), 3):
        l1 = list(data[line])
        l2 = list(data[line + 1])
        l3 = list(data[line + 2])

        for s in l1:
            if s in l2 and s in l3:
                letters.append(s)
                break

    for l in letters:
        num = (ord(l) - 96)
        if num <= 0:
            num = (ord(l.lower()) - 96) + 26
        total += num

    return total


user = User(token="")
puzzle = Puzzle(year=2022, day=3, user=user)
input_data = puzzle.input_data.splitlines()

puzzle.answer_a = part_1(input_data)
puzzle.answer_b = part_2(input_data)
puzzle.solve()
