import re

with open("./input/4") as file:
    lines = [line.rstrip() for line in file]

points = []
for line in lines:
    cleaned = line.split(": ")[1]
    a_list, b_list = [re.split(r"\s+", x.strip()) for x in cleaned.split(" | ")]
    intersection = [x for x in a_list if x in b_list]
    if len(intersection) > 0:
        points.append(pow(2, len(intersection) - 1))

print("Part 1: ", sum(points))
