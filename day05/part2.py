import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.is_horizontal = start.y == end.y
        self.is_vertical = start.x == end.x
        self.is_diagonal = abs(start.x - end.x) == abs(start.y - end.y)
        self.points = self.extract_covered_points()

    def extract_covered_points(self):
        if self.is_horizontal:
            if self.start.x < self.end.x:
                points = [(x, self.start.y) for x in list(range(self.start.x, self.end.x + 1))]
            else:
                points = [(x, self.start.y) for x in list(range(self.end.x, self.start.x + 1))]
        elif self.is_vertical:
            if self.start.y < self.end.y:
                points = [(self.start.x, y) for y in list(range(self.start.y, self.end.y + 1))]
            else:
                points = [(self.start.x, y) for y in list(range(self.end.y, self.start.y + 1))]
        elif self.is_diagonal:
            if self.start.x < self.end.x:
                x_range = list(range(self.start.x, self.end.x + 1))
            else:
                x_range = list(range(self.start.x, self.end.x - 1, -1))
            if self.start.y < self.end.y:
                y_range = list(range(self.start.y, self.end.y + 1))
            else:
                y_range = list(range(self.start.y, self.end.y - 1, -1))
            points = list(zip(x_range, y_range))
        else:
            points = []

        return points


def compute(s: str) -> int:
    lines = s.splitlines()
    lines_end_points = [[[int(point)
                          for point in points_pair.split(",")]
                         for points_pair in line.split(" -> ")]
                        for line in lines]

    lines = [Line(Point(*start), Point(*end)) for start, end in lines_end_points]

    all_points = {}
    for line in lines:
        for point in line.points:
            if point in all_points:
                all_points[point] += 1
            else:
                all_points[point] = 1

    count_overlap_points = 0
    for point, count in all_points.items():
        if count > 1:
            count_overlap_points += 1

    return count_overlap_points


INPUT_S = '''\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''
EXPECTED = 12


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
