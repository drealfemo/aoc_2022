def line(x0, y0, x1, y1):
    """Bresenham's line algorithm"""
    points_in_line = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    if dx > dy:
        err = dx / 2.0
        while x != x1:
            points_in_line.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            points_in_line.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    points_in_line.append((x, y))
    return points_in_line


def get_stone_points(track):
    s_track = []
    i = 0
    while True:
        if len(track) > 1:
            s_track += line(*track[i], *track[i+1])
            track.pop(0)
        else:
            break
    return s_track


def go_down(a, b):
    return a, b+1


def go_down_left(a, b):
    return a-1, b+1


def go_down_right(a, b):
    return a+1, b+1


if __name__ == "__main__":
    with open("input.txt") as f:
        tracks = [[list(map(int, x.split(","))) for x in line.split(" -> ")] for line in f.read().splitlines()]
    stone_pos = []
    for t in tracks:
        stone_pos += get_stone_points(t)
    stone_pos = sorted(set(stone_pos))
    min_x, max_x = stone_pos[0][0], stone_pos[-1][0]
    stone_pos = sorted(stone_pos, key=lambda x: x[1])
    cache_stone_pos = stone_pos.copy()
    min_y, max_y = stone_pos[0][1], stone_pos[-1][1]

    space = True
    count = 0
    while space:
        x, y = 500, 0
        while True:
            if x < min_x or x > max_x or y > max_y:
                space = False
                break
            if (likely_pos := go_down(x, y)) not in stone_pos:
                x, y = go_down(likely_pos[0], likely_pos[1])
                x, y = (x, y) if (x, y) not in stone_pos else likely_pos
            elif (likely_pos := go_down_left(x, y)) not in stone_pos:
                x, y = likely_pos
            elif (likely_pos := go_down_right(x, y)) not in stone_pos:
                x, y = likely_pos
            else:
                if x < min_x or x > max_x or y > max_y:
                    space = False
                else:
                    stone_pos.append((x, y))
                    count += 1
                break
    print(count)  # part 1

    stone_pos = cache_stone_pos
    min_y, max_y = stone_pos[0][1], stone_pos[-1][1] + 2
    space = True
    count = 0
    while space:
        x, y = 500, 0
        while True:
            if (likely_pos := go_down(x, y)) not in stone_pos and y+1 < max_y:
                if likely_pos[1] < max_y:
                    x, y = go_down(likely_pos[0], likely_pos[1])

                if (x, y) not in stone_pos and y < max_y:
                    x, y = x, y
                else:
                    x, y = likely_pos
            elif (likely_pos := go_down_left(x, y)) not in stone_pos and y+1 < max_y:
                if likely_pos[1] < max_y:
                    x, y = likely_pos
            elif (likely_pos := go_down_right(x, y)) not in stone_pos and y+1 < max_y:
                if likely_pos[1] < max_y:
                    x, y = likely_pos
            else:
                if (x, y) == (500, 0):
                    space = False
                else:
                    stone_pos.append((x, y))
                    count += 1
                break
    print(count+1)  # part 2 (very slow solution)

