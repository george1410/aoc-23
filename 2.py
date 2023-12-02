import re

with open("./input/2") as file:
    lines = [line.rstrip() for line in file]

max_red = 12
max_green = 13
max_blue = 14

possible = []
powers = []

for line in lines:
    game_id, results = line.split(": ")
    id = int(re.search(r"\d+", game_id).group())
    games = results.split("; ")
    is_impossible = False
    biggest = {"red": 0, "green": 0, "blue": 0}
    for game in games:
        colours = game.split(", ")
        pairs = [x.split(" ") for x in colours]
        counts = {k: int(v) for v, k in pairs}
        biggest["red"] = max(counts.get("red", 0), biggest["red"])
        biggest["green"] = max(counts.get("green", 0), biggest["green"])
        biggest["blue"] = max(counts.get("blue", 0), biggest["blue"])
        if (
            counts.get("red", 0) > max_red
            or counts.get("green", 0) > max_green
            or counts.get("blue", 0) > max_blue
        ):
            is_impossible = True
    if not is_impossible:
        possible.append(id)
    powers.append(biggest["blue"] * biggest["green"] * biggest["red"])

print("Part 1: ", sum(possible))
print("Part 2: ", sum(powers))
