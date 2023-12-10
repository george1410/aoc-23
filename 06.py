from functools import reduce

with open("./input/6") as file:
    lines = [line.rstrip() for line in file]

times = [x for x in lines[0].split(": ")[1].split()]
distances = [x for x in lines[1].split(": ")[1].split()]


def run_race(time, distance):
    return reduce(
        lambda acc, cur: acc + 1 if cur * (time - cur) > distance else acc,
        range(time),
    )


print(
    "Part 1: ",
    reduce(
        lambda a, b: a * b, [run_race(int(x), int(y)) for x, y in zip(times, distances)]
    ),
)
print("Part 2: ", run_race(int("".join(times)), int("".join(distances))))
