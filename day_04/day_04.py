import os
import sys


class Range:
    def __init__(self, range_input):
        self.start, self.stop = range_input.split("-")
        self.range = set(range(int(self.start), int(self.stop)+1))

    def is_duplicate(self, other):
        return self.range.issubset(other.range)

    def is_overlap(self, other):
        return not self.range.isdisjoint(other.range)


def part1(sections_pairs):
    duplicates = [
        x for x in sections_pairs if Range(x[0]).is_duplicate(Range(x[1])) or Range(x[1]).is_duplicate(Range(x[0]))
    ]
    return len(duplicates)


def part2(sections_pairs):
    overlaps = [x for x in sections_pairs if Range(x[0]).is_overlap(Range(x[1]))]
    return len(overlaps)


if __name__ == "__main__":
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        pairs = [x.split(",") for x in f.read().splitlines()]

    print(part1(pairs))
    print(part2(pairs))
