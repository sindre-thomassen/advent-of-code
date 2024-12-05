import re

def part1(INPUT):
    mul_operations = re.findall("mul\(\d+,\d+\)", INPUT)
    return sum([__mul(operation) for operation in mul_operations])

def part2(INPUT):
    operator = OperationHandler()

    pattern = "mul\(\d+,\d+\)|do\(\)|don't\(\)"
    opertations = re.findall(pattern, INPUT)

    for operation in opertations:
        operator.handle_operator(operation)

    return operator.VALUE

def __mul(operation):
    a, b = map(int, re.findall("\d+", operation))
    return a * b


class OperationHandler:
    ACTIVE = True
    VALUE = 0

    def handle_operator(self, operation):
        if operation == 'do()':
            self.ACTIVE = True
        elif operation == "don't()":
            self.ACTIVE = False
        elif self.ACTIVE:
            self.handle_mul(operation)

    def handle_mul(self, operation):
        a, b = map(int, re.findall("\d+", operation))
        self.VALUE += a * b

if __name__=="__main__":
    with open("input.txt", "r") as file:
        INPUT = file.read().strip()

    print(part1(INPUT))
    print(part2(INPUT))