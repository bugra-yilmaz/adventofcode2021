import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def get_neighbours(i, j, length, row_count):
    neighbours = [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
    neighbours = [neighbour for neighbour in neighbours
                  if -1 < neighbour[0] < row_count and -1 < neighbour[1] < length]
    return neighbours


def compute(s: str) -> int:
    lines = s.splitlines()
    height_map = [[int(n) for n in list(line)] for line in lines]

    low_points = []
    length = len(height_map[0])
    row_count = len(height_map)
    for i in range(row_count):
        for j in range(length):
            neighbours = get_neighbours(i, j, length, row_count)
            if all(height_map[i][j] < height_map[neighbour[0]][neighbour[1]] for neighbour in neighbours):
                low_points.append(height_map[i][j] + 1)

    return sum(low_points)


INPUT_S = '''\
2199943210
3987894921
9856789892
8767896789
9899965678
'''
EXPECTED = 15


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
