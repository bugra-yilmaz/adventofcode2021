import os.path
import statistics

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    positions = [int(n) for n in lines[0].split(",")]

    median = int(statistics.median(positions))
    return sum(abs(p - median) for p in positions)


INPUT_S = '''\
16,1,2,0,4,2,7,1,2,14
'''
EXPECTED = 37


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
