def solver(datastream, unique_count=4):
    start_of_packet = datastream[:unique_count-1]
    for char in datastream[unique_count-1:]:
        start_of_packet.append(char)
        if len(set(start_of_packet[-unique_count:])) == unique_count:
            return len(start_of_packet)


if __name__ == "__main__":
    with open("input.txt") as f:
        stream = list(f.readline())

    print(solver(stream))  # part 1
    print(solver(stream, unique_count=14))  # part 2
