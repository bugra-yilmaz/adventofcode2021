import os.path
from collections import defaultdict
from collections import deque

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    connections = defaultdict(lambda: set())
    for line in lines:
        cave1, cave2 = line.split("-")
        connections[cave1].add(cave2)
        connections[cave2].add(cave1)

    paths = deque()
    paths.append((["start"], False))
    final_paths = []
    while paths:
        path, has_visited_small_cave_twice = paths.popleft()
        if path[-1] == "end":
            final_paths.append(path)
            continue
        next_caves = connections[path[-1]]
        for next_cave in next_caves:
            if next_cave.isupper() or next_cave not in path or next_cave not in ["start", "end"] and \
                    not has_visited_small_cave_twice:
                if next_cave in path and next_cave.islower():
                    paths.append((path + [next_cave], True))
                else:
                    paths.append((path + [next_cave], has_visited_small_cave_twice))

    return len(final_paths)


INPUT_S = '''\
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
'''
EXPECTED = 3509


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
