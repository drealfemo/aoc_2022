import os
import sys
import string


ITEM_SCORE_MAP = dict(zip(list(string.ascii_lowercase[:26]) + list(string.ascii_uppercase[:26]), range(1, 53)))


def part1(rucksacks):
    total_score = 0
    for rucksack in rucksacks:
        midpoint = len(rucksack) // 2
        total_score += ITEM_SCORE_MAP[set(rucksack[:midpoint]).intersection(rucksack[midpoint:]).pop()]
    return total_score


def part2(rucksacks):
    total_score = 0
    for i in range(0, len(rucksacks), 3):
        group_sacks = rucksacks[i:i+3]
        total_score += ITEM_SCORE_MAP[set(group_sacks[0]).intersection(group_sacks[1]).intersection(group_sacks[2]).pop()]
    return total_score


if __name__ == "__main__":
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        bags = f.read().splitlines()
    print(part1(bags))
    print(part2(bags))
