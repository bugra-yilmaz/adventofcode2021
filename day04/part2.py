import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()

    numbers = [int(n) for n in lines[0].split(",")]

    boards = []
    board = []
    for line in lines[2:]:
        if len(board) == 5:
            boards.append(board)
            board = []
            continue
        row = [int(n.strip()) for n in line.split()]
        board.append(row)
    boards.append(board)
    original_length = len(boards)

    boards2 = []
    for board in boards:
        board2 = []
        for i in range(5):
            row2 = []
            for row in board:
                row2.append(row[i])
            board2.append(row2)
        boards2.append(board2)
    boards.extend(boards2)

    marks = {i: {j: 0 for j in range(len(boards[0]))} for i in range(len(boards))}
    marked_numbers = []
    winning_boards = set()
    for number in numbers:
        marked_numbers.append(number)
        for i in range(len(boards)):
            if i not in winning_boards:
                for j in range(5):
                    if number in boards[i][j]:
                        marks[i][j] += 1
                        if marks[i][j] == 5:
                            winning_boards.add(i)
                            if i < original_length:
                                winning_boards.add(i + original_length)
                            else:
                                winning_boards.add(i - original_length)

                            if len(winning_boards) == len(boards):
                                board_numbers = [number for row in boards[i] for number in row]
                                remaining_numbers = set(board_numbers) - set(marked_numbers)
                                return number * sum(remaining_numbers)


INPUT_S = '''\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''
EXPECTED = 1924


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    with open(INPUT_TXT, "r") as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
