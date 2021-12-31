import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    target_x = [int(x) for x in s.strip().split(", ")[0].split("=")[1].split("..")]
    target_y = [int(x) for x in s.strip().split(", ")[1].split("=")[1].split("..")]

    v_xs = [v_x for v_x in range(1, target_x[1] + 1) if is_in_target_area_x(v_x, target_x)]
    min_v_y = target_y[0]
    total_count = 0
    for v_x in v_xs:
        v_y = min_v_y
        count = 0
        velocities = []
        while True:
            if is_in_target_area((v_x, v_y), target_x, target_y):
                velocities.append((v_x, v_y))
            elif velocities:
                count += 1
            if count > 10:
                break
            v_y += 1
        total_count += len(velocities)

    return total_count


def is_in_target_area(velocity, target_x, target_y):
    trajectory = get_trajectory(velocity)
    min_x, max_x = target_x
    min_y, max_y = target_y
    while True:
        x, y = next(trajectory)

        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True

        elif x > max_x or y < min_y:
            return False


def get_trajectory(velocity):
    position = (0, 0)
    while True:
        v_x, v_y = velocity
        position = position[0] + v_x, position[1] + v_y
        if v_x:
            v_x = v_x - 1 if v_x > 0 else v_x + 1
        v_y -= 1
        velocity = (v_x, v_y)
        yield position


def is_in_target_area_x(v_x, target_x):
    trajectory = get_trajectory_x(v_x)
    min_x, max_x = target_x
    previous_x = 0
    while True:
        x = next(trajectory)

        if min_x <= x <= max_x:
            return True

        elif x > max_x:
            return False

        if previous_x == x:
            return False

        previous_x = x


def get_trajectory_x(v_x):
    p_x = 0
    while True:
        p_x = p_x + v_x
        if v_x:
            v_x = v_x - 1 if v_x > 0 else v_x + 1
        yield p_x


INPUT_S = '''\
target area: x=20..30, y=-10..-5
'''
EXPECTED = 112


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
