import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    length = len(lines[0])

    for i in range(length):
        lines_by_bit = {0: [], 1: []}
        count = 0
        for j, line in enumerate(lines):
            bits = [int(b) for b in line]
            if bits[i] == 1:
                count += 1
                lines_by_bit[1].append(j)
            else:
                count -= 1
                lines_by_bit[0].append(j)

        if count > -1:
            indexes = sorted(lines_by_bit[0], reverse=True)
        else:
            indexes = sorted(lines_by_bit[1], reverse=True)

        for index in indexes:
            del lines[index]

        if len(lines) == 1:
            oxygen = int(lines[0], 2)
            break

    lines = s.splitlines()
    for i in range(length):
        lines_by_bit = {0: [], 1: []}
        count = 0
        for j, line in enumerate(lines):
            bits = [int(b) for b in line]
            if bits[i] == 1:
                count += 1
                lines_by_bit[1].append(j)
            else:
                count -= 1
                lines_by_bit[0].append(j)

        if count > -1:
            indexes = sorted(lines_by_bit[1], reverse=True)
        else:
            indexes = sorted(lines_by_bit[0], reverse=True)

        for index in indexes:
            del lines[index]

        if len(lines) == 1:
            co2 = int(lines[0], 2)
            break

    return oxygen * co2


INPUT_S = '''\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''
EXPECTED = 230


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
