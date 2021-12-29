import os.path
from collections import Counter

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    polymer, pairs = s.split("\n\n")
    pairs = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in pairs.splitlines()}

    for _ in range(10):
        index = 0
        length = len(polymer)
        new_polymer = ""
        while index < length - 1:
            pair = polymer[index:index+2]
            new_polymer += pair[0] + pairs[pair]
            index += 1
        new_polymer += polymer[-1]
        polymer = new_polymer

    counts = Counter(polymer)

    return counts.most_common()[0][1] - counts.most_common()[-1][1]


INPUT_S = '''\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
'''
EXPECTED = 1588


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
