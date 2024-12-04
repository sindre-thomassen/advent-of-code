#!/usr/bin/python3
from Day4_1 import __PADDING__, get_input, prepare_data, create_pattern, find_matches

if __name__ == "__main__":
    input_data = get_input("./input.txt")
    prepared_data = prepare_data(input_data)

    m = len(input_data)
    n = len(input_data[0])+len(__PADDING__)  #length of padding

    patterns1 = [
        create_pattern("MAS", n),  # \ diagonal down
        create_pattern("MAS", n, True), # \ diagonal up
    ]
    patterns2 = [
        create_pattern("MAS", n-2),  # \ diagonal down
        create_pattern("MAS", n-2, True),  # \ diagonal up
    ]

    _, puzzle1 = find_matches(prepared_data, patterns1)
    _, puzzle2 = find_matches(prepared_data, patterns2)

    matching_A = [i for i in range(len(puzzle1)) if puzzle1[i] == "A" and puzzle2[i] == "A"]

    print(len(matching_A))