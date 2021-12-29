import os.path
from collections import defaultdict

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    polymer, pairs = s.split("\n\n")
    pairs = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in pairs.splitlines()}
    pair_counts = {pair: 0 for pair in pairs}
    for i in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        pair_counts[pair] += 1

    for _ in range(40):
        new_pair_counts = {pair: 0 for pair in pairs}

        for pair in pairs:
            element = pairs[pair]
            new_pair_counts[pair[0] + element] += pair_counts[pair]
            new_pair_counts[element + pair[1]] += pair_counts[pair]

        pair_counts = new_pair_counts

    letter_counts = defaultdict(lambda: 0)
    for pair in pairs:
        letter_counts[pair[0]] += pair_counts[pair]
        letter_counts[pair[1]] += pair_counts[pair]

    letter_counts[polymer[0]] += 1
    letter_counts[polymer[-1]] += 1

    letter_counts = {letter: count // 2 for letter, count in letter_counts.items()}

    return max(letter_counts.values()) - min(letter_counts.values())


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
EXPECTED = 2188189693529


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
