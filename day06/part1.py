import os.path
from collections import Counter

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    numbers = Counter(int(f) for f in lines[0].split(","))

    for d in range(80):
        numbers2 = Counter({8: numbers[0], 6: numbers[0]})
        for k, v in numbers.items():
            if k >= 1:
                numbers2[k - 1] += v
        numbers = numbers2
    return sum(numbers.values())


INPUT_S = '''\
3,4,3,1,2
'''
EXPECTED = 5934


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
