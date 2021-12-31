import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    target_x = [int(x) for x in s.strip().split(", ")[0].split("=")[1].split("..")]
    target_y = [int(x) for x in s.strip().split(", ")[1].split("=")[1].split("..")]

    v_x_mins = get_v_x_mins(target_x)
    v_y_maxs = []
    for v_x in v_x_mins:
        v_ys = []
        v_y = 1
        count = 0
        while True:
            if is_in_target_area((v_x, v_y), target_x, target_y):
                v_ys.append(v_y)
                count = 0
            elif v_ys:
                count += 1
            if count > 10:
                break
            v_y += 1
        v_y_maxs.append(max(v_ys))
    v_y_max = max(v_y_maxs)

    return sum(range(1, v_y_max + 1))


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


def get_v_x_mins(target_x):
    v_x_min = []
    v_x = 1
    while True:
        if is_in_target_area_x(v_x, target_x):
            end_x = sum(range(1, v_x + 1))
            if target_x[0] <= end_x <= target_x[1]:
                v_x_min.append(v_x)
        elif v_x_min:
            break
        v_x += 1

    return v_x_min


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
EXPECTED = 45


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
