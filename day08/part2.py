import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()

    sum_ = 0
    for line in lines:
        start, end = line.split(" | ")
        digits_all = {*start.split(), *end.split()}
        digits = {"".join(sorted(digit)) for digit in digits_all}

        one, = (digit for digit in digits if len(digit) == 2)
        four, = (digit for digit in digits if len(digit) == 4)
        seven, = (digit for digit in digits if len(digit) == 3)
        eight, = (digit for digit in digits if len(digit) == 7)
        two, = (digit for digit in digits
                if len(digit) == 5 and
                len(set(digit) & set(four)) == 2)
        three, = (digit for digit in digits
                  if len(digit) == 5 and
                  len(set(digit) - set(two)) == 1)
        five, = (digit for digit in digits
                 if len(digit) == 5 and
                 len(set(digit) - set(two)) == 2)
        nine, = (digit for digit in digits
                 if len(digit) == 6 and
                 len(set(digit) - set(four)) == 2)
        six, = (digit for digit in digits
                if len(digit) == 6 and
                len(set(nine) - set(digit) & set(one)) == 1)
        zero, = (digit for digit in digits
                 if len(digit) == 6 and
                 set(digit) != set(nine) and set(digit) != set(six))

        decoding = {zero: "0", one: "1", two: "2", three: "3", four: "4",
                    five: "5", six: "6", seven: "7", eight: "8", nine: "9"}

        output = int("".join([decoding["".join(sorted(digit))] for digit in end.split()]))
        sum_ += output

    return sum_


INPUT_S = '''\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''
EXPECTED = 61229


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
