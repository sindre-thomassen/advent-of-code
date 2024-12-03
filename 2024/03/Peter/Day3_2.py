#!/usr/bin/python3
import re
from typing import List, Tuple
from Day3_1 import get_input, parse_input

def find_valid_mul(line: str) -> List[Tuple[int,int]]:
    pattern = r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)"
    matches = re.finditer(pattern, line)
    do = True
    valid_mul: List[Tuple[int,int]] = list()
    for match in matches:
        group = match.group()
        if group == "do()":
            do = True
        elif group == "don't()":
            do = False
        else:
            if do:
                groups = match.groups()
                valid_mul.append((int(groups[0]), int(groups[1])))
    return valid_mul

if __name__ == "__main__":
    input_data = get_input()
    lists = parse_input(input_data)
    result = sum(a*b for a,b in find_valid_mul(lists))

    print(result)