import functools
import collections

with open("./input/7") as file:
    lines = [line.rstrip() for line in file]

hands = [tuple(x.split()) for x in lines]


def get_type(hand):
    counts = collections.Counter(hand)
    if len(counts) == 1:
        return 7
    elif len(counts) == 2:
        return 6 if counts[hand[0]] == 1 or counts[hand[0]] == 4 else 5
    elif len(counts) == 3:
        return (
            4
            if counts[hand[0]] != 2 and counts[hand[1]] != 2 and counts[hand[2]] != 2
            else 3
        )
    elif len(counts) == 4:
        return 2
    else:
        return 1


rankings = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def sort_hands(a, b):
    a_type = get_type(a[0])
    b_type = get_type(b[0])
    if a_type != b_type:
        return b_type - a_type
    else:
        for i in range(len(a[0])):
            if rankings.index(a[0][i]) != rankings.index(b[0][i]):
                return rankings.index(b[0][i]) - rankings.index(a[0][i])


sorted_hands = list(reversed(sorted(hands, key=functools.cmp_to_key(sort_hands))))

winnings = [(i + 1) * int(y) for i, (x, y) in enumerate(sorted_hands)]

print("Part 1: ", sum(winnings))
