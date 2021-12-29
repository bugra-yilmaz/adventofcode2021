import os.path
from collections import deque

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    rows = s.splitlines()
    length = len(rows)
    width = len(rows[0])

    risks = {(i, j): int(risk) for i, row in enumerate(rows) for j, risk in enumerate(row)}
    destination = (length - 1, width - 1)

    paths = deque([(0, 0)])
    lowest_risks_by_position = {(0, 0): 0}
    while paths:
        position = paths.popleft()
        risk = lowest_risks_by_position[position]

        if position == destination:
            continue

        for point in get_adjacent(position, length, width):
            new_path = point
            new_risk = risk + risks[point]
            if point not in lowest_risks_by_position or lowest_risks_by_position[point] > new_risk:
                lowest_risks_by_position[point] = new_risk
                paths.append(new_path)

    return lowest_risks_by_position[destination]


def get_adjacent(point, length, width):
    i, j = point
    adjacent = [(i + 1, j),
                (i, j + 1),
                (i, j - 1),
                (i - 1, j)]

    return ((i, j) for i, j in adjacent if -1 < i < length and -1 < j < width)


INPUT_S = '''\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
'''
EXPECTED = 40


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
