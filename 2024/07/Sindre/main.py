OPERATORS = {
    'x': lambda x, y: x * y,
    '+': lambda x, y: x + y,
    '|': lambda x, y: int(str(x) + str(y))
}


def part_1(INPUT):
    score = 0

    for answer, values in INPUT:
        # Uncomment to make slightly faster (maybe?)

        # ---------------------------------------------------------------------------
        # # Check highest possible value (only multiplication except if value = 1)
        # operators = 'x' if values[0] > 1 else '+'
        # for i in range(2, len(values)):
        #     if values[i] > 1:
        #         operators += 'x'
        #     else:
        #         operators += '+'
        #
        # tmp = _process(values, operators)
        #
        # # Highest possible value is exactly target
        # if tmp == answer:
        #     score += answer
        #     continue
        #
        # # Highest possible value is under target
        # if tmp < answer:
        #     continue
        #
        # # Check lowest possible value (only addition except if value = 1)
        # operators = operators.replace('x', '_').replace('+', 'x').replace('_', '+')
        # tmp = _process(values, operators)
        #
        # # Lowest possible value is exactly target
        # if tmp == answer:
        #     score += answer
        #     continue
        #
        # # Lowest possible value is over target
        # if tmp > answer:
        #     continue
        # ---------------------------------------------------------------------------

        # Check all other possibilities
        possible = _recursive_search(0, values, answer, 0)
        if possible:
            score += answer

    return score


# Same as part 1 but with concatenation operator
def part_2(INPUT):
    score = 0
    for answer, values in INPUT:
        possible = _recursive_search(0, values, answer, 0, True)
        if possible:
            score += answer

    return score


def _process(values, operators):
    result = values[0]
    for i in range(1, len(values)):
        result = OPERATORS[operators[i-1]](result, values[i])

    return result


def _recursive_search(current_value, values, target, index, concat=False):
    # Initialize current value
    if index == 0:
        return _recursive_search(values[index], values, target, index + 1, concat)

    # Reached end of values. Have not found target
    if index == len(values):
        return False

    # Calculate new current value and compare to target
    for operator in '+x' if not concat else '+x|':
        new_value = OPERATORS[operator](current_value, values[index])
        if new_value == target and index == len(values) - 1:
            return True
        if new_value > target:
            continue

        new_value = _recursive_search(new_value, values, target, index + 1, concat)
        if new_value:
            return True

    return False

if __name__=='__main__':
    with open("input.txt", "r") as file:
        lines = [line.strip().split(':') for line in file.readlines()]
        INPUT = [
            (int(line[0]), [int(x) for x in line[1].strip().split(' ')]) for line in lines
        ]

    print(part_1(INPUT))
    print(part_2(INPUT))