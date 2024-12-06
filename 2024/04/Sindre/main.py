import numpy as np

from Sindre import _INPUT
from Sindre.directions import check_horizontally, check_vertically, check_diagonally, check_cross


def part1(INPUT):
    # Should find all instances of string XMAS in 2D array
    Xs = np.argwhere(INPUT == "X")

    cases = 0
    for x in Xs:
        y, x = x
        cases += check_horizontally(INPUT, x, y)
        cases += check_vertically(INPUT, x, y)
        cases += check_diagonally(INPUT, x, y)

    return cases

def part2(INPUT):
    score = 0

    As = np.argwhere(INPUT == "A")
    for y, x in As:
        score += int(check_cross(INPUT, x, y))

    return score

if __name__=="__main__":
    print(part1(_INPUT))
    print(part2(_INPUT))