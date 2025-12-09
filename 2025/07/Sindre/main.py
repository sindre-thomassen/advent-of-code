import numpy as np
import time as t


TEST = False
PRINT = False

with open("./inputs/test.txt" if TEST else "./inputs/input.txt", "r") as file:
    MAP = np.array([list(line.strip()) for line in file.readlines()])


##### Part 1 #####

def compare_and_update(beam, line):
    # Should return (score, new_beam)

    if not '^' in line:
        return 0, beam


    should_split = beam & (line == '^')

    new_beam = beam.copy()
    split_indices = np.where(should_split)
    for i in split_indices:
        new_beam[i-1] = True
        new_beam[i+1] = True

    new_beam[line=='^'] = False

    return sum(should_split), new_beam

start = t.time()

beam = MAP[0]=='S'
total = 0

for line in MAP[1:]:
    score, beam = compare_and_update(beam, line)
    total += score

    if PRINT:
        tmp = line.copy()
        tmp[beam] = '|'
        print(''.join(tmp).replace('.', ' '))

print(f"Part 1: {total:15} ({(t.time()-start)*1000:.2f} ms)")





##### Part 2 #####

# Traverse the map as before, but keep track of number of ways to reach each point of the map, propagating these scores downwards
# When split, if two splits on the same line meet, this point's score should double
def compare_and_score(beam, line, current_scores):
    # No splits on this line. Return as is
    if not '^' in line:
        return current_scores, beam

    should_split = beam & (line == '^')

    new_beam = beam.copy()
    new_scores = current_scores.copy() # Propagate existing scores where not split, set score to 0 where split
    split_indices = np.where(should_split)

    for i in split_indices:
        new_beam[i-1] = True
        new_beam[i+1] = True

    new_beam[line=='^'] = False

    # Update scores
    for i in split_indices:
        new_scores[i-1] += current_scores[i]
        new_scores[i+1] += current_scores[i]
        new_scores[i] = 0

    return new_scores, new_beam

start = t.time()

beam = MAP[0]=='S'
scores = np.zeros_like(beam, dtype=np.int64)
scores[beam] = 1  # Start with one way to reach the starting point
total_paths = 0

for line in MAP[1:]:
    scores, beam = compare_and_score(beam, line, scores)

print(f"Part 2: {sum(scores):15} ({(t.time()-start)*1000:.2f} ms)")