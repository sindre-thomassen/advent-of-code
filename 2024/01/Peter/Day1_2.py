#!/usr/bin/python3

from typing import List, Tuple
from collections import Counter

from Day1_1 import get_input, parse_input

if __name__ == "__main__":
    input_data = get_input()
    lists = [sorted(list(l)) for l in parse_input(input_data)]

    counts: List[Counter] = [Counter(l) for l in lists]

    # ids only found in one list will be ignored due to multiply with 0 from one side adds nothing to total score
    ids_in_both = set(counts[0].keys()).intersection(set(counts[1].keys()))
    result = sum(id * counts[0].get(id) * counts[1].get(id) for id in ids_in_both)

    print(result)