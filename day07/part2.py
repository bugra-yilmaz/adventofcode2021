import os.path
import statistics

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def get_cost_for_target(target, positions):
    return sum(abs(p - target) * (abs(p - target) + 1) // 2 for p in positions)


def compute(s: str) -> int:
    lines = s.splitlines()
    positions = [int(n) for n in lines[0].split(",")]

    mean = int(statistics.mean(positions))

    if get_cost_for_target(mean - 1, positions) < get_cost_for_target(mean, positions):
        direction = -1
    else:
        direction = 1

    while get_cost_for_target(mean + direction, positions) < get_cost_for_target(mean, positions):
        mean += direction

    return get_cost_for_target(mean, positions)


INPUT_S = '''\
16,1,2,0,4,2,7,1,2,14
'''
EXPECTED = 168


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
