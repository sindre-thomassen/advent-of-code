import numpy as np


def part1(INPUT):
    safe = 0

    for row in INPUT:
        row = np.array(row)
        diff = row[1:] - row[:-1]
        if np.all(((diff > 0) & (diff <= 3))) or np.all(((diff < 0) & (diff >= -3))):
            safe += 1

    return safe


def part2(INPUT):
    safe = 0

    for row in INPUT:
        row = np.array(row)
        for piv in range(len(row)):
            tmp = np.delete(row, piv)

            diff = tmp[1:] - tmp[:-1]
            if np.all(((diff > 0) & (diff <= 3))) or np.all(((diff < 0) & (diff >= -3))):
                safe += 1
                break

    return safe


if __name__=="__main__":
    with open("input.txt", "r") as file:
        INPUT = [[int(x) for x in line.split()] for line in file.readlines()]

    print(part1(INPUT))
    print(part2(INPUT))
