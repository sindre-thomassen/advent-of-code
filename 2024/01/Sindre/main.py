import numpy as np

def part1(INPUT):
    INPUT = np.array(INPUT)
    return abs(np.sort(INPUT[:, 0])-np.sort(INPUT[:, 1])).sum()


def part2(INPUT):
    INPUT = np.array(INPUT)
    X = INPUT[:, 0]
    Y = INPUT[:, 1]

    score = 0
    for i in X:
        score += i * sum(Y == i)

    return score

if __name__=="__main__":
    file = open("input.txt", "r")
    INPUT = [[int(x) for x in line.split()] for line in file.readlines()]
    file.close()
    print(part1(INPUT))
    print(part2(INPUT))
