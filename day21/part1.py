import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    player1_s, player2_s = s.splitlines()
    player1_p, player2_p = int(player1_s.split(": ")[1]), int(player2_s.split(": ")[1])

    player1_score, player2_score = 0, 0
    dice = 1
    while True:
        player1_p = (player1_p + 3 * dice + 3 - 1) % 10 + 1
        player1_score += player1_p
        dice += 3
        if player1_score >= 1000:
            break

        player2_p = (player2_p + 3 * dice + 3 - 1) % 10 + 1
        player2_score += player2_p
        dice += 3
        if player2_score >= 1000:
            break

    return (dice - 1) * min(player1_score, player2_score)


INPUT_S = '''\
Player 1 starting position: 4
Player 2 starting position: 8
'''
EXPECTED = 739785


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
