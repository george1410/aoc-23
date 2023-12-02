import re

with open("./input/1") as file:
    lines = [line.rstrip() for line in file]

numbers = [None, "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def get_digit(num):
    return str(num if num.isnumeric() else numbers.index(num))


def solve(pattern):
    nums = [re.findall(pattern, x) for x in lines]
    joined = [int(get_digit(x[0]) + get_digit(x[-1])) for x in nums]
    return sum(joined)


print("Part 1: ", solve(r"\d"))
print("Part 2: ", solve(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"))
