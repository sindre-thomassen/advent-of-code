#!/usr/bin/python3
import re
from typing import List, Tuple

__PADDING__ = "____"


def get_input(filename:str) -> List[str]:
    with open(filename) as file:
        lines = file.read().splitlines()
        return lines

def prepare_data(data: List[str]) -> str:
    result_data = list()
    for line in data:
        result_data.append(line+__PADDING__) #add padding to prevent false positives on diagonals
    return "".join(result_data)

def find_matches(data: str, patterns: List[Tuple[str,int]]) -> Tuple[int, str]:
    matches = 0
    out_data = "."*len(data)

    for pattern, dist in patterns:
        # trickery due to standard re not supporting overlapping matches
        lookup_index = 0
        while True:
            found = re.finditer(pattern, data[lookup_index:])
            has_match = False
            for match in found:
                has_match = True
                matches += 1
                start = match.regs[0][0] + lookup_index
                end = match.regs[0][1] + lookup_index
                while start < end:
                    out_data = out_data[:start] + data[start] + out_data[start+1:]
                    start += dist + 1
                lookup_index += match.regs[0][0]+1
                break
            if not has_match:
                break
    return matches, out_data

def create_pattern(p:str, count: int, reverse: bool= False) -> Tuple[str,int]:
    if reverse:
        p = p[::-1]
    return ("."*count).join(list(p)), count

def print_puzzle(puzzle: str, n: int):
    def wrap(s, w):
        return [s[i:i + w] for i in range(0, len(s), w)]

    lines = wrap(puzzle, n)
    lines = [line[:n-len(__PADDING__)] for line in lines]
    print("\n".join(lines))

if __name__ == "__main__":
    input_data = get_input("./input.txt")
    prepared_data = prepare_data(input_data)

    m = len(input_data)
    n = len(input_data[0])+len(__PADDING__)  #length of padding

    patterns = [
        create_pattern("XMAS",0), # normal
        create_pattern("XMAS",0, True), # reverse
        create_pattern("XMAS", n-1), # down
        create_pattern("XMAS", n-1, True),  # up
        create_pattern("XMAS", n),  # \ diagonal down
        create_pattern("XMAS", n, True), # \ diagonal up
        create_pattern("XMAS", n-2),  # \ diagonal down
        create_pattern("XMAS", n-2, True),  # \ diagonal up
    ]

    result, puzzle = find_matches(prepared_data, patterns)
    print_puzzle(puzzle, n)
    print(result)