import numpy as np

def part_1(INPUT):
    INPUT = np.array(INPUT)

    # (next_position, starting_position, altitude)
    queue = [((int(x), int(y)), (int(x), int(y)), 0) for x, y in np.argwhere(INPUT == "0")]

    reachable_peaks = []

    # For each start = 0, find any reachable 9s with a steady incline
    while queue:
        pos, start, altitude = queue.pop(0)
        x, y = pos
        if INPUT[x, y] == "9":
            reachable_peaks.append((pos, start))
            continue

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_pos = (x+dx, y+dy)
            if 0 <= new_pos[0] < INPUT.shape[0] and 0 <= new_pos[1] < INPUT.shape[1] and INPUT[new_pos] != ".":
                if INPUT[new_pos] == str(altitude+1):
                    queue.append((new_pos, start, altitude+1))

    return len(set(reachable_peaks))

def part_2(INPUT):
    INPUT = np.array(INPUT)

    # (next_position, starting_position, altitude)
    queue = [(pos, 0) for pos in np.argwhere(INPUT == "0")]

    reachables = 0

    # For each start = 0, find all distinct trails ending on 9s with a steady incline
    while queue:
        pos, altitude = queue.pop(0)
        x, y = pos
        if INPUT[x, y] == "9":
            reachables += 1
            continue

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_pos = (x+dx, y+dy)
            if 0 <= new_pos[0] < INPUT.shape[0] and 0 <= new_pos[1] < INPUT.shape[1] and INPUT[new_pos] != ".":
                if INPUT[new_pos] == str(altitude+1):
                    queue.append((new_pos, altitude+1))

    return reachables

if __name__=="__main__":
    with open("input.txt", "r") as file:
        INPUT = [list(line.strip()) for line in file]

    print(part_1(INPUT))
    print(part_2(INPUT))