import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str):
    dot_s, fold_s = s.split("\n\n")
    dots = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in dot_s.splitlines()]
    folds = [(line.split("=")[0][-1], int(line.split("=")[1])) for line in fold_s.splitlines()]

    for axis, value in folds:
        if axis == "x":
            to_remove = []
            for i, dot in enumerate(dots):
                if dot[0] > value:
                    dots[i] = (value - (dot[0] - value), dot[1])
                elif dot[0] == value:
                    to_remove.append(dot)
            dots = list(set(dots) - set(to_remove))
        else:
            to_remove = []
            for i, dot in enumerate(dots):
                if dot[1] > value:
                    dots[i] = (dot[0], value - (dot[1] - value))
                elif dot[1] == value:
                    to_remove.append(dot)
            dots = list(set(dots) - set(to_remove))

    display_dots(dots)


def display_dots(dots):
    max_x = max([dot[0] for dot in dots])
    max_y = max([dot[1] for dot in dots])
    paper = []
    for i in range(max_y + 1):
        line = []
        for j in range(max_x + 1):
            if (j, i) in dots:
                line.append("#")
            else:
                line.append(",")
        paper.append(line)
    string = "\n".join(["".join(line) for line in paper])
    print(string)


def main() -> int:
    with open(INPUT_TXT, "r") as f:
        compute(f.read())

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
