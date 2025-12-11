import re
import time as t


TEST = False

with open("./inputs/test.txt" if TEST else "./inputs/input.txt", "r") as f:
    cases = []
    while (line:=f.readline().strip()):
        tmp = line.split()

        lights = set([i for i in range(len(tmp[0][1:-1])) if tmp[0][i+1] == "#"])
        buttons = [set(map(int, re.findall("\d+", button))) for button in tmp[1:-1]]
        joltages = list(map(int, re.findall("\d+", tmp[-1])))

        cases.append([lights, buttons, joltages])


start = t.time()

total_presses = 0

for target, buttons, _ in cases:
    states = [(set(), 0)]
    checked = []
    found = False

    while len(states)>0 and not found:
        state, presses = states.pop(0)
        if state in checked:
            continue
        checked.append(state)

        if state == target:
            found = True
            total_presses += presses
            break

        for i, button in enumerate(buttons):
            new_state = state ^ button
            if new_state == target:
                total_presses += presses + 1
                found = True
                break

            if new_state not in states and new_state not in checked:
                states.append((new_state, presses + 1))


print(f"Part 1: Solved in {total_presses} presses ({t.time() - start:.5f} seconds)")


##### Part 2 #####

# Part 2 uses the "joltages" where each button increases the joltage of each index in the button by 1
# Find the least amount of presses to reach the target state where all joltages matches the target joltages


