import os.path
from collections import Counter
from collections import defaultdict

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    player1_s, player2_s = s.splitlines()
    player1_p, player2_p = int(player1_s.split(": ")[1]), int(player2_s.split(": ")[1])

    player1_score, player2_score = 0, 0
    dice = list(Counter(i + j + k for i in range(1, 4) for j in range(1, 4) for k in range(1, 4)).items())
    situations = {(player1_p, player1_score, player2_p, player2_score): 1}
    player1_wins = 0
    player2_wins = 0
    while situations:
        new_situations = defaultdict(int)
        for situation, count in situations.items():
            player1_p, player1_score, player2_p, player2_score = situation
            for dice_number1, dice_count1 in dice:
                player1_p_new = (player1_p + dice_number1 - 1) % 10 + 1
                player1_score_new = player1_score + player1_p_new
                if player1_score_new >= 21:
                    player1_wins += count * dice_count1
                    continue

                for dice_number2, dice_count2 in dice:
                    player2_p_new = (player2_p + dice_number2 - 1) % 10 + 1
                    player2_score_new = player2_score + player2_p_new
                    if player2_score_new >= 21:
                        player2_wins += count * dice_count1 * dice_count2
                        continue

                    new_situations[(player1_p_new, player1_score_new, player2_p_new, player2_score_new)] += \
                        count * dice_count1 * dice_count2

        situations = new_situations

    return max(player1_wins, player2_wins)


INPUT_S = '''\
Player 1 starting position: 4
Player 2 starting position: 8
'''
EXPECTED = 444356092776315


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
