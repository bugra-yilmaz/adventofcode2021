import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    row_count = len(lines)
    length = len(lines[0])

    energies = {}
    for i, line in enumerate(lines):
        for j, n in enumerate(line):
            energies[(i, j)] = int(n)

    count = 0
    for _ in range(100):
        flash = []
        for (x, y) in energies:
            if energies[(x, y)] == 9:
                energies[(x, y)] = 0
                flash.append((x, y))
            else:
                energies[(x, y)] += 1
        count += len(flash)

        while flash:
            new_flash = []
            for (x, y) in flash:
                for (x_, y_) in get_adjacent((x, y), length, row_count):
                    if energies[(x_, y_)] == 9:
                        energies[(x_, y_)] = 0
                        new_flash.append((x_, y_))
                    elif energies[(x_, y_)] == 0:
                        energies[(x_, y_)] = 0
                    else:
                        energies[(x_, y_)] += 1
            count += len(new_flash)
            flash = new_flash

    return count


def get_adjacent(position: tuple[int, int], row_count: int, length: int) -> list[tuple[int, int]]:
    position_x, position_y = position
    potential_adjacent = [(position_x - 1, position_y - 1),
                          (position_x - 1, position_y),
                          (position_x, position_y - 1),
                          (position_x + 1, position_y),
                          (position_x, position_y + 1),
                          (position_x - 1, position_y + 1),
                          (position_x + 1, position_y - 1),
                          (position_x + 1, position_y + 1)]
    adjacent = [(x, y) for x, y in potential_adjacent if -1 < x < row_count and -1 < y < length]

    return adjacent


def display_energies(energies: dict[tuple[int, int], int], row_count: int, length: int):
    string = ""
    for i in range(row_count):
        line = ""
        for j in range(length):
            line += str(energies[(i, j)])
        string += line + "\n"
    print(string)


INPUT_S = '''\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''
EXPECTED = 1656


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
