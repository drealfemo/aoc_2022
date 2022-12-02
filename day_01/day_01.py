import os
import sys


def get_max_calories(count=1):
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        calories = [sum(map(int, section.split("\n"))) for section in f.read().split('\n\n')]
        calories.sort(reverse=True)
        return sum(calories[:count])


if __name__ == '__main__':
    print(get_max_calories())  # part 1
    print(get_max_calories(3))  # part 2
