import os.path
from collections import defaultdict

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    algorithm, image_s = s.split("\n\n")
    algorithm = algorithm.replace("#", "1").replace(".", "0")
    image_s = image_s.split()

    i_min, i_max = -1, len(image_s) + 2
    j_min, j_max = -1, len(image_s[0]) + 2
    image = defaultdict(lambda: "0")
    for i, _ in enumerate(image_s):
        for j, pixel in enumerate(image_s[i]):
            image[(i, j)] = "1" if pixel == "#" else "0"

    for k in range(2):
        count = 0

        if k % 2 == 0:
            output_image = defaultdict(lambda: algorithm[0])
        else:
            output_image = defaultdict(lambda: algorithm[511])

        for i in range(i_min, i_max):
            for j in range(j_min, j_max):
                pixels = get_window(i, j)
                values = [image[(x, y)] for x, y in pixels]
                output_value = algorithm[int("".join(values), 2)]
                output_image[(i, j)] = output_value
                count = count + 1 if output_value == "1" else count
        i_min -= 1
        j_min -= 1
        i_max += 1
        j_max += 1
        image = output_image

    return count


def get_window(i, j):
    return [(i - 1, j - 1),
            (i - 1, j),
            (i - 1, j + 1),
            (i, j - 1),
            (i, j),
            (i, j + 1),
            (i + 1, j - 1),
            (i + 1, j),
            (i + 1, j + 1)]


INPUT_S = '''\
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
'''
EXPECTED = 35


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
