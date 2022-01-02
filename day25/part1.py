import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()

    row_count = len(lines)
    col_count = len(lines[0])
    south_herd = set()
    east_herd = set()
    for i, row in enumerate(lines):
        for j, point in enumerate(row):
            if point == "v":
                south_herd.add((i, j))
            elif point == ">":
                east_herd.add((i, j))

    count = 0
    while True:
        moved = False

        new_east_herd = set()
        for i, j in east_herd:
            if j == col_count - 1:
                next_j = 0
            else:
                next_j = j + 1

            if (i, next_j) not in east_herd and (i, next_j) not in south_herd:
                new_east_herd.add((i, next_j))
                moved = True
            else:
                new_east_herd.add((i, j))
        east_herd = new_east_herd

        new_south_herd = set()
        for i, j in south_herd:
            if i == row_count - 1:
                next_i = 0
            else:
                next_i = i + 1

            if (next_i, j) not in east_herd and (next_i, j) not in south_herd:
                new_south_herd.add((next_i, j))
                moved = True
            else:
                new_south_herd.add((i, j))
        south_herd = new_south_herd

        count += 1

        if not moved:
            break

    return count


INPUT_S = '''\
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
'''
EXPECTED = 58


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
