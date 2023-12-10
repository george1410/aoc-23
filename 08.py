import re
from itertools import count

with open("./input/8") as file:
    lines = [line.rstrip() for line in file]

instructions, _, *rest = lines

pattern = r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)"
mapping = {
    x.groups()[0]: (x.groups()[1], x.groups()[2])
    for x in re.finditer(pattern, "\n".join(lines))
}


def traverse(start, instructions):
    cur = start
    for i in count():
        inst = instructions[i % len(instructions)]
        cur = mapping[cur][0] if inst == "L" else mapping[cur][1]

        if cur == "ZZZ":
            return i + 1


print("Part 1: ", traverse("AAA", instructions))
