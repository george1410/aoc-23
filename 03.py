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


adjacents = defaultdict(list)
for index, line in enumerate(lines):
    matches = re.finditer(r"\d+", line)
    for match in matches:
        surrounding = check_surrounding(match, index)
        if surrounding is None:
            continue
        adjacents[surrounding].append(int(match.group()))

part_numbers = [item for x in adjacents.values() for item in x]
gear_ratios = [v[0] * v[1] for k, v in adjacents.items() if len(v) == 2 and k[2] == "*"]

print("Part 1: ", sum(part_numbers))
print("Part 2: ", sum(gear_ratios))
