import numpy as np
from tqdm import tqdm

with open("input.txt") as f:
    objects = []

    while (line := f.readline().strip()):
        cylinders = [list(line)]
        for _ in range(6):
            line = f.readline().strip()
            cylinders.append(list(line))

        f.readline()
        objects.append(np.array(cylinders))

locks, keys = [], []

for object in objects:
    if np.all(object[0] == "#"):
        locks.append((object == "#").sum(axis=0) - 1)
    else:
        keys.append((object == "#").sum(axis=0) - 1)

valid_combinations = 0

locks = np.array(locks)
for key in tqdm(keys):
    valid_combinations += ((locks + key) < 6).all(axis=1).sum()

print(valid_combinations)