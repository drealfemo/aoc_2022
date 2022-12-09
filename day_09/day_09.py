def get_tail_position(h_p, t_p):
    if h_p[0] == t_p[0]:  # same row
        # right
        if h_p[1] - t_p[1] == 2:
            return [t_p[0], t_p[1]+1]
        # left
        elif h_p[1] - t_p[1] == -2:
            return [t_p[0], t_p[1]-1]
        else:
            return t_p
    elif h_p[1] == t_p[1]:  # same col
        # up
        if h_p[0] - t_p[0] == -2:
            return [t_p[0]-1, t_p[1]]
        # down
        elif h_p[0] - t_p[0] == 2:
            return [t_p[0]+1, t_p[1]]
        else:
            return t_p
    else:  # diagonals
        # up 2 right 1
        if h_p[0] - t_p[0] == -2 and h_p[1] - t_p[1] == 1:
            return [t_p[0]-1, t_p[1]+1]
        # up 1 right 2
        elif h_p[0] - t_p[0] == -1 and h_p[1] - t_p[1] == 2:
            return [t_p[0]-1, t_p[1]+1]
        # up 2 left 1
        elif h_p[0] - t_p[0] == -2 and h_p[1] - t_p[1] == -1:
            return [t_p[0]-1, t_p[1]-1]
        # up1 left 2
        elif h_p[0] - t_p[0] == -1 and h_p[1] - t_p[1] == -2:
            return [t_p[0]-1, t_p[1]-1]
        # down 2 right 1
        elif h_p[0] - t_p[0] == 2 and h_p[1] - t_p[1] == 1:
            return [t_p[0]+1, t_p[1]+1]
        # down 1 right 2
        elif h_p[0] - t_p[0] == 1 and h_p[1] - t_p[1] == 2:
            return [t_p[0]+1, t_p[1]+1]
        # down 2 left
        elif h_p[0] - t_p[0] == 2 and h_p[1] - t_p[1] == -1:
            return [t_p[0]+1, t_p[1]-1]
        # down-left 2
        elif h_p[0] - t_p[0] == 1 and h_p[1] - t_p[1] == -2:
            return [t_p[0]+1, t_p[1]-1]

        # up 2 right 2
        elif h_p[0] - t_p[0] == -2 and h_p[1] - t_p[1] == 2:
            return [t_p[0] - 1, t_p[1] + 1]
        # up 2 left 2
        elif h_p[0] - t_p[0] == -2 and h_p[1] - t_p[1] == -2:
            return [t_p[0] - 1, t_p[1] - 1]
        # down 2 right 2
        elif h_p[0] - t_p[0] == 2 and h_p[1] - t_p[1] == 2:
            return [t_p[0] + 1, t_p[1] + 1]
        # down 2 left 2
        elif h_p[0] - t_p[0] == 2 and h_p[1] - t_p[1] == -2:
            return [t_p[0] + 1, t_p[1] - 1]
        else:
            return t_p


def solver(commands, count=2, key=1):
    knots = [[15, 11] for _ in range(count)]
    unique_tail_pos = {k: set() for k in range(1, count)}
    for cmd in commands:
        for _ in range(cmd[1]):
            i = 0
            while i < count-1:
                h_pos, t_pos = knots[i], knots[i+1]
                if i == 0:
                    if cmd[0] == "R":
                        h_pos[1] += 1
                    elif cmd[0] == "L":
                        h_pos[1] -= 1
                    elif cmd[0] == "U":
                        h_pos[0] -= 1
                    elif cmd[0] == "D":
                        h_pos[0] += 1
                t_pos = get_tail_position(h_pos, t_pos)
                knots[i] = h_pos
                knots[i+1] = t_pos
                unique_tail_pos[i+1].add(tuple(t_pos))
                i += 1
    return len(unique_tail_pos[key])


if __name__ == "__main__":
    with open("input.txt") as f:
        cmds = [x.split(" ") for x in f.read().splitlines()]
    cmds = [[x[0], int(x[1])] for x in cmds]
    print(solver(cmds))
    print(solver(cmds, count=10, key=9))
