def part1(tree_grid, start_row, end_row, start_col, end_col, seen):
    visible = 0
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            tree = tree_grid[row][col]
            # left
            if max(tree_grid[row][:col]) < tree:
                visible += 1
                continue
            # right
            if max(tree_grid[row][col+1:]) < tree:
                visible += 1
                continue
            # up
            if max([x[col] for x in tree_grid[:row]]) < tree:
                visible += 1
                continue
            # down
            if max([x[col] for x in tree_grid[row+1:]]) < tree:
                visible += 1
                continue
    return visible + seen


def part2(tree_grid, start_row, end_row, start_col, end_col):
    max_seen = 0
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            tree = tree_grid[row][col]
            l_s, r_s, u_s, d_s = 0, 0, 0, 0
            # left
            for t in (tree_grid[row][:col])[::-1]:
                l_s += 1
                if tree <= t:
                    break
            # right
            for t in tree_grid[row][col+1:]:
                r_s += 1
                if tree <= t:
                    break
            # up
            for t in [x[col] for x in tree_grid[:row]][::-1]:
                u_s += 1
                if tree <= t:
                    break
            # down
            for t in [x[col] for x in tree_grid[row+1:]]:
                d_s += 1
                if tree <= t:
                    break
            seen = l_s * r_s * u_s * d_s
            max_seen = max(max_seen, seen)
    return max_seen


if __name__ == "__main__":
    with open("input.txt") as f:
        grid = [list(map(int, list(x))) for x in f.read().splitlines()]
    row_length, col_length = len(grid), len(grid[0])
    already_seen = (2 * (row_length - 2)) + (2 * col_length)
    s_row, s_col = 1, 1
    e_row, e_col = row_length - 2, col_length - 2
    print(part1(grid, s_row, e_row, s_col, e_col, already_seen))
    print(part2(grid, s_row, e_row, s_col, e_col))
