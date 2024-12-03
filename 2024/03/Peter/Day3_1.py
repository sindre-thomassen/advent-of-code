#!/usr/bin/python3
import re
from typing import List, Tuple

def get_input() -> List[str]:
    with open("./input.txt") as file:
        lines = file.read().splitlines()
        return lines

def parse_input(lines: List[str]) -> str:
    return "".join(lines)

def find_valid_mul(line: str) -> List[Tuple[int, int]]:
    matches = re.findall(r"mul\((\d+),(\d+)\)", line)
    return [(int(a), int(b)) for a, b in matches]

if __name__ == "__main__":
    input_data = get_input()
    lists = parse_input(input_data)
    result = sum(a*b for a,b in find_valid_mul(lists))

    print(result)

