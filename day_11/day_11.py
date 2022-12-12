if __name__ == "__main__":
    with open("sample_input.txt") as f:
        inputs = f.read().splitlines()

    monkey_items = {}
    monkey_operation = {}
    monkey_test = {}
    monkey_action = {}

    for i in range(0, len(inputs), 7):
        monkey = inputs[i].split("Monkey ")[1][:-1]
        monkey_items[monkey] = list(map(int, inputs[i + 1].split("Starting items: ")[1].split(", ")))
        monkey_operation[monkey] = eval("lambda old: (" + inputs[i + 2].split("Operation: new = ")[1] + ") // 3 ")
        monkey_test[monkey] = int(inputs[i + 3].split(" ")[-1])
        monkey_action[monkey] = [inputs[i + 4].split(" ")[-1], inputs[i + 5].split(" ")[-1]]
    monkey_inspections = {k: 0 for k in monkey_items}
    i = 0
    while i < 20:
        for monkey in monkey_items:
            for item in monkey_items[monkey]:
                monkey_inspections[monkey] += 1
                item = monkey_operation[monkey](item)
                actions = monkey_action[monkey]
                if item % monkey_test[monkey] == 0:
                    monkey_items[actions[0]].append(item)
                else:
                    monkey_items[actions[1]].append(item)
            monkey_items[monkey] = []
        i += 1
    top_two_inspections = sorted(monkey_inspections.values())[-2:]
    print(top_two_inspections[0] * top_two_inspections[1])