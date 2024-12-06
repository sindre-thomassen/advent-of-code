#!/usr/bin/python3
import re
from typing import List, Tuple, Set, Dict
from functools import cmp_to_key


def get_input(filename:str) -> List[str]:
    with open(filename) as file:
        lines = file.read().splitlines()
        return lines

def prepare_data(data: List[str]) -> Tuple[Set[Tuple[int,int]], List[List[int]]]:
    sort_rules = set()
    page_list = list()
    rules = True
    pages = False
    for line in data:
        if rules:
            if line == "":
                rules = False
                pages = True
                continue
            rule = re.findall(r'\d+', line)
            sort_rules.add((int(rule[0]),int(rule[1])))
        elif pages:
            page = list(map(int, line.split(',')))
            page_list.append(page)
    return sort_rules, page_list

def create_sort_function(sort_rules: Set[Tuple[int,int]]):
    before: Dict[int, Set[int]] = dict()
    after: Dict[int, Set[int]] = dict()

    def sort_function(a, b) -> int:
        if a in before and b in before[a]:
            return -1
        if a in after and b in after[a]:
            return 1

    for rule in sort_rules:
        if rule[0] not in before:
            before[rule[0]] = set()
        before[rule[0]].add(rule[1])
        if rule[1] not in after:
            after[rule[1]] = set()
        after[rule[1]].add(rule[0])

    return cmp_to_key(sort_function)

def check_if_correct(manual: List[int], sort_function)-> Tuple[bool, List[int]]:
    sorted_list = manual.copy()
    sorted_list.sort(key=sort_function)
    return sorted_list == manual, sorted_list

if __name__ == "__main__":
    input_data = get_input("./input.txt")
    page_rules, page_list = prepare_data(input_data)
    sort_function = create_sort_function(page_rules)
    result = 0
    for manual in page_list:
        correct, _ = check_if_correct(manual, sort_function)
        if correct:
            result += manual[len(manual)//2]
    print(result)