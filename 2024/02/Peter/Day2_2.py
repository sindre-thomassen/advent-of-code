#!/usr/bin/python3

from typing import List
from Day2_1 import get_input, parse_input, check_report

def check_report_dampener(report: List[int]) -> bool:
    if check_report(report):
        return True
    for i in range(len(report)):
        if check_report(report[:i] + report[i+1:]):
            return True
    return False


if __name__ == "__main__":
    input_data = get_input()
    lists = parse_input(input_data)
    result = sum(check_report_dampener(l) for l in lists)

    print(result)