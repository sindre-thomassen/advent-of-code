from itertools import combinations

import numpy as np

def part_1(INPUT):
    INPUT = np.array(INPUT)
    uniques = set((tmp := INPUT.flatten())[tmp != "."])
    anticells = []

    for freq in uniques:
        antennas = np.argwhere(INPUT == freq)
        if len(antennas) == 0:
            continue

        for A, B in combinations(antennas, 2):
            diff = B - A
            new_anticell = tuple(B + diff)
            if new_anticell[0] >= 0 and new_anticell[1] >= 0 and new_anticell[0] < INPUT.shape[0] and new_anticell[1] < INPUT.shape[1]:
                anticells.append(new_anticell)

            new_anticell = tuple(A - diff)
            if new_anticell[0] >= 0 and new_anticell[1] >= 0 and new_anticell[0] < INPUT.shape[0] and new_anticell[1] < INPUT.shape[1]:
                anticells.append(new_anticell)

    return len(set(anticells))



def part_2(INPUT):
    INPUT = np.array(INPUT)
    uniques = set((tmp := INPUT.flatten())[tmp != "."])
    anticells = []

    for freq in uniques:
        antennas = np.argwhere(INPUT == freq)
        if len(antennas) == 0:
            continue

        for A, B in combinations(antennas, 2):
            diff = B - A
            pos = _find_smallest(A, diff, INPUT.shape)
            while _is_inside(pos, INPUT.shape):
                anticells.append(tuple(pos))
                pos += diff

    return len(set(anticells))

# Find smallest x and y possible from given delta-x and delta-y
def _find_smallest(start: np.array, delta, shape):
    pos = start.copy()
    while _is_inside(pos-delta, shape):
        pos -= delta

    return pos

def _is_inside(pos, shape):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < shape[0] and pos[1] < shape[1]

if __name__=="__main__":
    with open("input.txt", "r") as file:
        lines = file.readlines()
        INPUT = [list(line.strip()) for line in lines]

    print(part_1(INPUT))
    print(part_2(INPUT))
