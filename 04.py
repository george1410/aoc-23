from collections import defaultdict

with open("./input/4") as file:
    lines = [line.rstrip() for line in file]

points = []
counts = defaultdict(int)
for index, line in enumerate(lines):
    counts[index + 1] += 1
    cleaned = line.split(": ")[1]
    a_list, b_list = [x.split() for x in cleaned.split(" | ")]
    intersection = [x for x in a_list if x in b_list]
    if len(intersection) > 0:
        points.append(pow(2, len(intersection) - 1))
        for i in range(len(intersection)):
            counts[i + index + 2] += 1 * counts[index + 1]

print("Part 1: ", sum(points))
print("Part 2: ", sum(counts.values()))
