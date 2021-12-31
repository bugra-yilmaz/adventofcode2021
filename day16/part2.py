import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    packet = s.strip()

    packet = "".join([hexadecimal_to_binary(c) for c in packet])
    versions = []

    _, value = parse_packet(versions, packet, 0)

    return value


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

        return index, int(value, 2)

    else:
        values = []
        length_type_id = int(packet[index:index + 1], 2)
        index += 1

        if length_type_id == 0:
            length = int(packet[index:index + 15], 2)
            index += 15
            end = index + length

            while index < end:
                index, value = parse_packet(versions, packet, index)
                values.append(value)

        else:
            count = int(packet[index:index + 11], 2)
            index += 11

            for _ in range(count):
                index, value = parse_packet(versions, packet, index)
                values.append(value)

        if type_id == 0:
            value = sum(values)
        elif type_id == 1:
            value = 1
            for v in values:
                value *= v
        elif type_id == 2:
            value = min(values)
        elif type_id == 3:
            value = max(values)
        elif type_id == 5:
            value = 1 if values[0] > values[1] else 0
        elif type_id == 6:
            value = 1 if values[0] < values[1] else 0
        else:
            value = 1 if values[0] == values[1] else 0

        return index, value


def hexadecimal_to_binary(hexadecimal: str) -> str:
    return bin(int(hexadecimal, 16))[2:].zfill(4)


INPUT_S = '''\
9C0141080250320F1802104A08
'''
EXPECTED = 1


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
