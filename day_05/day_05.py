import re


def get_col_data(inputs):
    fil_inputs = []
    inputs = inputs.split("\n")
    for line in inputs:
        if line[1] != "1":
            fil_line = []
            for pos in range(1, len(line), 4):
                fil_line.append(line[pos])
            fil_inputs.append(fil_line)

    rows = len(fil_inputs)
    cols = max(len(x) for x in fil_inputs)
    col_inputs = [[0] * rows for _ in range(cols)]
    for i in range(len(col_inputs)):
        col = []
        for row in fil_inputs:
            try:
                val = row[i] if row[i] else None
            except:
                val = None
            if val and val != " ":
                col.append(val)
        col_inputs[i] = col[::-1]
    return col_inputs


def get_instructions(instructions):
    instructions_rgx = re.compile("move ([0-9]+) from ([0-9]+) to ([0-9]+)")
    instructions = instructions.split("\n")
    instructions = [re.match(instructions_rgx, x).groups() for x in instructions]
    return instructions


def crate_mover(new_model=False):
    col_data = get_col_data(input_arr)
    instructions = get_instructions(commands)
    for cmd in instructions:
        cmd = list(map(int, cmd))
        quantity = cmd[0]
        temp = []
        for i in range(quantity):
            if not new_model or quantity == 1:
                col_data[cmd[2] - 1].append(col_data[cmd[1] - 1].pop())
            else:
                temp.append(col_data[cmd[1] - 1].pop())
        if temp:
            col_data[cmd[2] - 1].extend(temp[::-1])
    return "".join([col.pop() for col in col_data])


if __name__ == "__main__":
    with open("input.txt") as f:
        input_arr, commands = f.read().split("\n\n")

    print(crate_mover())  # part 1
    print(crate_mover(new_model=True))  # part 2
