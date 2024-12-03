#!/usr/bin/python3

from typing import List, Tuple

def get_input() -> List[str]:
    with open("./input.txt") as file:
        lines = file.read().splitlines()
        return lines

def parse_input(lines: List[str]) -> List[Tuple[int]]:
    return list(zip(*(map(int, line.split()) for line in lines)))

if __name__ == "__main__":
    input_data = get_input()
    lists = [sorted(list(l)) for l in parse_input(input_data)]
    result = sum(abs(a-b) for a,b in zip(lists[0], lists[1]))

    print(result)