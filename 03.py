from collections import defaultdict
from re import Match
import re

with open("./input/3") as file:
    lines = [line.rstrip() for line in file]


def check_line(line: int, start: int, end: int):
    if match := re.search(r"[^\d\.]", lines[line][start : end + 1]):
        return (match.start() + start, line, match.group())


def check_surrounding(match: Match, line: int):
    start = max(match.start() - 1, 0)
    end = match.end()

    if res := check_line(line, start, end):
        return res
    if line > 0 and (res := check_line(line - 1, start, end)):
        return res
    if line < len(lines) - 1 and (res := check_line(line + 1, start, end)):
        return res


part_numbers = []
star_adjacents = defaultdict(list)
for index, line in enumerate(lines):
    matches = re.finditer(r"\d+", line)
    for match in matches:
        surrounding = check_surrounding(match, index)
        if surrounding is None:
            continue
        part_numbers.append(int(match.group()))
        if surrounding[2] == "*":
            star_adjacents[surrounding].append(int(match.group()))

gear_ratios = [v[0] * v[1] for v in star_adjacents.values() if len(v) == 2]

print("Part 1: ", sum(part_numbers))
print("Part 2: ", sum(gear_ratios))
