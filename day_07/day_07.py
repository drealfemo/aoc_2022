def get_dir_sizes(terminal_output):
    child_parent_map = {}
    dir_sizes = {}
    lines = len(terminal_output)
    i = 0
    history = ["/"]
    cd = None
    while i != lines:
        line = terminal_output[i]
        if line.startswith("$ cd") and not line.endswith(".."):
            cd = line.split("$ cd ")[1]
            if cd != "/":
                cd = history[-1] + cd + "/"
                history.append(cd)
            if cd not in dir_sizes:
                dir_sizes[cd] = 0
        elif line.endswith(".."):
            history.pop(-1)
            cd = history[-1]
        elif line[0].isdigit():
            size = int(line.split(" ")[0])
            dir_sizes[cd] += size
            child = cd
            while parent := child_parent_map.get(child):
                dir_sizes[parent] += size
                child = parent
        elif "dir " in line:
            child_parent_map[history[-1] + line.split(" ")[1] + "/"] = cd
        i += 1
    return dir_sizes


def part1(dir_sizes):
    res_dict = {k: v for k, v in dir_sizes.items() if v <= 100000}
    return sum(res_dict.values())


def part2(dir_sizes):
    unused_space = 7e7 - dir_sizes["/"]
    needed_space = 3e7 - unused_space
    likely_dirs = {k: v for k, v in dir_sizes.items() if v >= needed_space}
    final_dir = min(likely_dirs, key=likely_dirs.get)
    return likely_dirs[final_dir]


if __name__ == "__main__":
    with open("input.txt") as f:
        output = f.read().splitlines()

    sizes = get_dir_sizes(output)
    print(part1(sizes))
    print(part2(sizes))
