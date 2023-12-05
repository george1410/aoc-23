import itertools

with open("./input/5") as file:
    lines = [line.rstrip() for line in file]

seed_line, *rest_lines = lines
seeds = [int(x) for x in seed_line.split(": ")[1].split()]

labeled_groups = [
    list(y) for x, y in itertools.groupby(rest_lines, lambda z: z == "") if not x
]
groups = [[[int(z) for z in x.split()] for x in y[1:]] for y in labeled_groups]

locations = []
for seed in seeds:
    cur = seed
    for group in groups:
        for map in group:
            if cur >= map[1] and cur < map[1] + map[2]:
                cur = map[0] + cur - map[1]
                break
    locations.append(cur)

print("Part 1: ", min(locations))
