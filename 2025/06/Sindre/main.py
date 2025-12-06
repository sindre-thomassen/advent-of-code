from asyncio import new_event_loop

import numpy as np
import re

def recursive_add(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + recursive_add(numbers[1:])


def recursive_multiply(numbers):
    if len(numbers) == 0:
        return 1
    else:
        return max(1, numbers[0]) * recursive_multiply(numbers[1:])


##### Part 1 #####

TEST = False

with open("./inputs/test.txt" if TEST else "./inputs/input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    for i in range(len(lines)-1):
        lines[i] = list(map(int, re.findall(r'\d+', lines[i])))

    operands = re.findall("[+*]", lines.pop())

numbers = np.array(lines).T

total = 0

for number_list, operand in zip(numbers, operands):
    if operand == '+':
        result = recursive_add(number_list.tolist())
    elif operand == '*':
        result = recursive_multiply(number_list.tolist())

    total += result

print(f"Part 1: {total}")



##### Part 2 #####

with open("./inputs/test.txt" if TEST else "./inputs/input.txt", "r") as f:
    max_string_size = 0
    lines = []
    for line in f.readlines():
        max_string_size = max(max_string_size, len(line.replace('\n', '')))
        lines.append(line.replace('\n', ''))

    for i in range(len(lines)):
        lines[i] = lines[i][::-1].zfill(max_string_size)[::-1]

    operands = re.findall("[+*]", lines[-1])
    lines = lines[:-1]

    lines = np.array([list(line) for line in lines]).T

    lines[(lines == ' ').all(axis=1)] = '_'
    lines[lines==' '] = 0
    lines = np.array([''.join(line).split('_') for line in lines.T]).T


def process_numbers(numbers, operand):
    numbers = np.array(list(map(lambda x: list(x), numbers))).T

    new_numbers = []
    for numberline in numbers:
        new_numbers.append(int(''.join(numberline).replace('0', '')))

    if operand == '+':
        result = recursive_add(new_numbers)
    elif operand == '*':
        result = recursive_multiply(new_numbers)

    return result


total = 0
for numbers, operand in zip(lines, operands):
    total += process_numbers(numbers, operand)

print(f"Part 2: {total}")
