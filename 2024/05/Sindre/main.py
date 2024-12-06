from functools import reduce


def part_1(filepath):
    rules, cases = {}, []

    with open(filepath) as file:
        while (line := file.readline().strip()):
            new_rule = [int(x) for x in line.strip().split("|")]

            if new_rule[0] in rules.keys():
                rules[new_rule[0]].append(new_rule[1])
            else:
                rules[new_rule[0]] = [new_rule[1]]

        while (line := file.readline().strip()):
            cases.append([int(x) for x in line.strip().split(",")])

    valid_cases = []
    invalid_cases = []

    for case in cases:
        if validate_case(case[::-1], rules):
            valid_cases.append(case)
        else:
            invalid_cases.append(case)

    return rules, invalid_cases, reduce(lambda x, y: x + y[len(y)//2], valid_cases, 0)


def part_2(rules, invalid_cases):
    sorted_cases = [order(case, rules) for case in invalid_cases]
    return reduce(lambda x, y: x + y[len(y)//2], sorted_cases, 0)


def validate_case(case, rules):
    for i in range(len(case)-1):
        if case[i+1] in rules.get(case[i], []):
            return False
    return True


def order(case, rules):
    sorted_case = [0 for _ in case]
    for n in case:
        index = len(set(case).intersection(set(rules.get(n, []))))
        sorted_case[index] = n

    return sorted_case

if __name__=="__main__":
    rules, invalid_cases, res = part_1("input.txt")
    print(res)
    print(part_2(rules, invalid_cases))
