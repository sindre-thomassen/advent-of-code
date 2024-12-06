#!/usr/bin/python3

from Day5_1 import get_input, prepare_data, create_sort_function, check_if_correct

if __name__ == "__main__":
    input_data = get_input("./input.txt")
    page_rules, page_list = prepare_data(input_data)
    sort_function = create_sort_function(page_rules)
    result = 0
    for manual in page_list:
        correct, sorted_pages = check_if_correct(manual, sort_function)
        if not correct:
            result += sorted_pages[len(sorted_pages)//2]
    print(result)