import os
import re
import time
import shutil
import argparse
from datetime import datetime
from urllib import request
from urllib import error
from urllib import parse

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".token"), "r") as f:
    HEADERS = {"cookie": f.read()}

TOO_QUICK = re.compile("You gave an answer too recently.*to wait.")
WRONG = re.compile(r"That's not the right answer.*?\.")
RIGHT = "That's the right answer!"
ALREADY_DONE = re.compile(r"You don't seem to be solving.*\?")


def get_input(year: int, day: int) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    print(url)
    req = request.Request(url, headers=HEADERS)
    return request.urlopen(req).read().decode()


def get_current_year_day() -> tuple[int, int]:
    return datetime.now().year, datetime.now().day


def download_input_for_current_day() -> int:
    year, day = get_current_year_day()
    for i in range(5):
        try:
            s = get_input(year, day)
        except error.URLError as e:
            print(f"Input not ready yet: {e}.")
            time.sleep(1)
        else:
            break
    else:
        raise SystemExit("Timed out after attempting 5 times!")

    with open("input.txt", "w") as f:
        f.write(s)

    lines = s.splitlines()
    if len(lines) > 10:
        for line in lines[:10]:
            print(line)
        print("...")
    else:
        print(lines[0][:80])
        print("...")

    return 0


def submit_solution_for_current_day() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", "-p", type=int, required=True)
    parser.add_argument("--answer", "-a", type=int, required=True)
    args = parser.parse_args()

    year, day = get_current_year_day()

    params = parse.urlencode({"level": args.part, "answer": args.answer})
    req = request.Request(
        f"https://adventofcode.com/{year}/day/{day}/answer",
        method="POST",
        data=params.encode(),
        headers=HEADERS,
    )
    resp = request.urlopen(req)
    contents = resp.read().decode()

    for error_regex in (WRONG, TOO_QUICK, ALREADY_DONE):
        error_match = error_regex.search(contents)
        if error_match:
            print(f"\033[41m{error_match[0]}\033[m")
            return 1

    if RIGHT in contents:
        print(f"\033[42m{RIGHT}\033[m")
        return 0
    else:
        # unexpected output?
        print(contents)
        return 1


def prepare_question_for_current_day():
    _, day = get_current_year_day()
    cwd = os.path.dirname(os.path.abspath(__file__))
    source = f"{cwd}/template"
    destination = f"{cwd}/../day{day}"
    shutil.copytree(source, destination)
