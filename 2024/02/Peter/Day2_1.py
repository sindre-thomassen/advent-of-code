#!/usr/bin/python3

from typing import List

def get_input() -> List[str]:
    with open("./input.txt") as file:
        lines = file.read().splitlines()
        return lines

def parse_input(lines: List[str]) -> List[List[int]]:
    return [[int(x) for x in l.split()] for l in lines]

def check_report(report: List[int]) -> bool:
    increasing = sorted(report) == report
    decreasing = sorted(report, reverse=True) == report
    if not increasing and not decreasing:
        return False

    #loop though length 2 slices of the report
    for i in range(len(report)-1):
        # report is invalid if the difference between the two elements is not between 1 and 3
        if not 1<=abs(report[i+1] - report[i])<=3:
            return False
    return True


if __name__ == "__main__":
    input_data = get_input()
    lists = parse_input(input_data)
    result = sum(check_report(l) for l in lists)

    print(result)