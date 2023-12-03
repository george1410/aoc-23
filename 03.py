from collections import defaultdict
from re import Match
import re

with open("./input/3") as file:
    lines = [line.rstrip() for line in file]


def check_surrounding(match: Match, line: int):
    start = match.start()
    end = match.end()

    x_search_start = start - 1 if start > 0 else 0
    x_search_end = end + 1 if end < len(lines[line]) - 2 else end

    has_char = False
    if start > 0 and lines[line][x_search_start] != ".":
        has_char = True
        if lines[line][x_search_start] == "*":
            return (x_search_start, line)
    if end < len(lines[line]) - 1 and lines[line][end] != ".":
        has_char = True
        if lines[line][end] == "*":
            return (end, line)
    if line > 0:
        for index, char in enumerate(lines[line - 1][x_search_start:x_search_end]):
            if char != ".":
                has_char = True
                if char == "*":
                    return (x_search_start + index, line - 1)
    if line < len(lines) - 1:
        for index, char in enumerate(lines[line + 1][x_search_start:x_search_end]):
            if char != ".":
                has_char = True
                if char == "*":
                    return (x_search_start + index, line + 1)
    if has_char:
        return True


part_numbers = []
star_adjacents = defaultdict(list)
for index, line in enumerate(lines):
    matches = re.finditer(r"\d+", line)
    for match in matches:
        surrounding = check_surrounding(match, index)
        if surrounding is not None:
            part_numbers.append(int(match.group()))
        if isinstance(surrounding, tuple):
            star_adjacents[surrounding].append(int(match.group()))

gear_ratios = [v[0] * v[1] for v in star_adjacents.values() if len(v) == 2]

print("Part 1: ", sum(part_numbers))
print("Part 2: ", sum(gear_ratios))
