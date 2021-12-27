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

    basins = []
    marked_points = set()
    length = len(height_map[0])
    row_count = len(height_map)
    for i in range(row_count):
        for j in range(length):
            if (i, j) not in marked_points:
                marked_points.add((i, j))
                if height_map[i][j] != 9:
                    basin = [(i, j)]
                    root = [(i, j)]
                    added = True
                    while added:
                        added = False
                        neighbours = set(
                            [neighbour for i, j in root for neighbour in get_neighbours(i, j, length, row_count)])
                        root = []
                        for neighbour in neighbours:
                            if neighbour not in marked_points:
                                marked_points.add(neighbour)
                                if height_map[neighbour[0]][neighbour[1]] != 9:
                                    basin.append(neighbour)
                                    added = True
                                    root.append(neighbour)
                    basins.append(basin)

    top3_basin_sizes = sorted(basins, key=lambda x: len(x), reverse=True)[:3]

    return len(top3_basin_sizes[0]) * len(top3_basin_sizes[1]) * len(top3_basin_sizes[2])


INPUT_S = '''\
2199943210
3987894921
9856789892
8767896789
9899965678
'''
EXPECTED = 1134


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
