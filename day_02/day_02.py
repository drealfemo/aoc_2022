import os
import sys


def part1(rounds):
    rps_map = {"A": "X", "B": "Y", "C": "Z"}
    win_rules = {("A", "Y"): 6, ("B", "Z"): 6, ("C", "X"): 6}
    rps_score = {"X": 1, "Y": 2, "Z": 3}
    choice_score = sum(rps_score[x] for _, x in plays)
    play_score = 0
    for play in rounds:
        if rps_map[play[0]] == play[1]:
            play_score += 3
        else:
            play_score += win_rules.get(play, 0)
    total_score = choice_score + play_score
    return total_score


def part2(rounds):
    rps_score = {"A": 1, "B": 2, "C": 3}
    win_rules = dict([("A", "B"), ("B", "C"), ("C", "A")])
    loss_rules = {v: k for k, v in win_rules.items()}
    choice_score = 0
    play_score = 0
    for play in rounds:
        if play[1] == "X":
            choice_score += rps_score[loss_rules[play[0]]]
        elif play[1] == "Y":
            choice_score += rps_score[play[0]]
            play_score += 3
        else:
            choice_score += rps_score[win_rules[play[0]]]
            play_score += 6
    total_score = choice_score + play_score
    return total_score


if __name__ == "__main__":
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        plays = [tuple(line.split(" ")) for line in f.read().splitlines()]

    print(part1(plays))
    print(part2(plays))

