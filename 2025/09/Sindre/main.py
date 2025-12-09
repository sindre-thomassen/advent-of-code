import numpy as np
from tqdm import tqdm

TEST = False


red_tiles = []

with open("./inputs/test.txt" if TEST else "./inputs/input.txt", "r") as f:
    for line in f.readlines():
        red_tiles.append(list(map(int, line.strip().split(','))))

red_tiles = np.array(red_tiles)

# Find the four most extreme points (top left, top right, bottom left, bottom right)
tr = red_tiles[np.argmax(red_tiles[:, 0] - red_tiles[:, 1])]
br = red_tiles[np.argmax(red_tiles[:, 0] + red_tiles[:, 1])]
tl = red_tiles[np.argmax(-red_tiles[:, 0] - red_tiles[:, 1])]
bl = red_tiles[np.argmax(-red_tiles[:, 0] + red_tiles[:, 1])]


##### Part 1 #####


max_area = 0

for tile in [tr, br, tl, bl]:
    score = np.max((tmp:=np.abs(tile - red_tiles)+1)[:, 0] * tmp[:, 1])
    max_area = score if score > max_area else max_area

print(f"Part 1: {max_area}")



##### Part 2 #####

# Need to find the largest rectangle defined by two points in the list which makes all the nodes in the rectangle stay inside the polygon defined by all points in the list
max_area = 0

from shapely import Polygon

polygon = Polygon(red_tiles)

max_area = 0
# Find the max area rectangle possible from each starting node (NOT each pair of nodes
for tile in tqdm(red_tiles):
    d = np.abs(red_tiles - tile) + 1
    sizes = (d[:, 0] * d[:, 1])
    if np.max(sizes) <= max_area:
        continue

    tmp = sorted(list(zip(sizes, red_tiles)), key=lambda x: x[0], reverse=True)

    for size, corner in tmp:
        if size <= max_area:
            break

        rect = Polygon([
            (tile[0], tile[1]),
            (tile[0], corner[1]),
            (corner[0], corner[1]),
            (corner[0], tile[1]),
        ])

        if polygon.contains(rect):
            max_area = size if size > max_area else max_area
            break

print(f"Part 2: {max_area}")
