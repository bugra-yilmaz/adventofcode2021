import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()

    matches = {"{": "}", "(": ")", "[": "]", "<": ">"}
    points = {"}": 3, ")": 1, "]": 2, ">": 4}

    scores = []
    for line in lines:
        is_corrupted = False
        if line[0] not in matches:
            continue
        opened = [line[0]]
        for c in line[1:]:
            if c in matches:
                opened.append(c)
            else:
                last_open = opened.pop()
                if matches[last_open] != c:
                    is_corrupted = True
                    break

        if not is_corrupted:
            closing = [matches[c] for c in opened[::-1]]
            score = 0
            for c in closing:
                score *= 5
                score += points[c]
            scores.append(score)

    return sorted(scores)[len(scores) // 2]


INPUT_S = '''\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''
EXPECTED = 288957


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
