if __name__ == "__main__":
    with open("input.txt") as f:
        instructions = f.read().splitlines()
    register = 1
    cycle = 0
    signal_strengths = {}
    crt = [["."]*40 for _ in range(6)]
    sprite_pos = (0, 1, 2)
    crt_row, crt_col = 0, 0

    for cmd in instructions:
        cycle += 1
        crt[crt_row][crt_col] = "#" if crt_col in sprite_pos else "."
        crt_col += 1
        if (cycle / 20) % 2 == 1:
            signal_strengths[cycle] = register * cycle
        elif (cycle / 20) % 2 == 0:
            crt_row += 1
            crt_col = 0
        if "noop" in cmd:
            continue
        elif "addx" in cmd:
            cycle += 1
            crt[crt_row][crt_col] = "#" if crt_col in sprite_pos else "."
            crt_col += 1
            if (cycle / 20) % 2 == 1:
                signal_strengths[cycle] = register * cycle
            elif (cycle / 20) % 2 == 0:
                crt_row += 1
                crt_col = 0
            register += int(cmd.split(" ")[1])
            sprite_pos = (register-1, register, register+1)
            continue
    # part 1
    print(sum(signal_strengths.values()))
    # part 2
    for row in crt:
        print(*row)
