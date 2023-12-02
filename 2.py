with open("./input/2") as file:
    lines = [line.rstrip() for line in file]

max_r, max_g, max_b = 12, 13, 14

possible = []
powers = []

for line in lines:
    game_id, results = line.split(": ")
    id = int(game_id.split(" ")[1])
    games = results.split("; ")
    maxi = {"r": 0, "g": 0, "b": 0}
    for game in games:
        colours = game.split(", ")
        pairs = [x.split(" ") for x in colours]
        counts = {k: int(v) for v, k in pairs}
        maxi["r"] = max(counts.get("red", 0), maxi["r"])
        maxi["g"] = max(counts.get("green", 0), maxi["g"])
        maxi["b"] = max(counts.get("blue", 0), maxi["b"])
    if maxi["r"] <= max_r and maxi["g"] <= max_g and maxi["b"] <= max_b:
        possible.append(id)
    powers.append(maxi["b"] * maxi["g"] * maxi["r"])

print("Part 1: ", sum(possible))
print("Part 2: ", sum(powers))
