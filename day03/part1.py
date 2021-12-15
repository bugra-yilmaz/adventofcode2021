import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()

    counts = {i: {0: 0, 1: 0} for i in range(len(lines[0]))}
    for line in lines:
        bits = [int(b) for b in line]
        for i, bit in enumerate(bits):
            if bit == 0:
                counts[i][0] += 1
            else:
                counts[i][1] += 1

    gamma = ""
    epsilon = ""
    for bit_order, values in counts.items():
        if values[0] > values[1]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return int(gamma, 2) * int(epsilon, 2)


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
EXPECTED = 198


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
