import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    packet = s.strip()
    packet = "".join([hexadecimal_to_binary(c) for c in packet])
    versions = []

    parse_packet(versions, packet, 0)

    return sum(versions)


def parse_packet(versions, packet, index):
    if "1" not in packet:
        return

    version = int(packet[index:index + 3], 2)
    versions.append(version)
    index += 3

    type_id = int(packet[index:index + 3], 2)
    index += 3

    if type_id == 4:
        value = ""
        while packet[index] == "1":
            value += packet[index + 1:index + 5]
            index += 5
        value += packet[index + 1:index + 5]
        index += 5

        return index

    else:
        length_type_id = int(packet[index:index + 1], 2)
        index += 1

        if length_type_id == 0:
            length = int(packet[index:index + 15], 2)
            index += 15
            end = index + length

            while index < end:
                index = parse_packet(versions, packet, index)

        else:
            count = int(packet[index:index + 11], 2)
            index += 11

            for _ in range(count):
                index = parse_packet(versions, packet, index)

        return index


def hexadecimal_to_binary(hexadecimal: str) -> str:
    return bin(int(hexadecimal, 16))[2:].zfill(4)


INPUT_S = '''\
A0016C880162017C3686B18A3D4780
'''
EXPECTED = 31


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
