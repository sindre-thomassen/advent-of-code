import numpy as np
import matplotlib.pyplot as plt

def part_1(INPUT):
    control = np.zeros((len(INPUT), len(INPUT[0])), dtype=str)

    total_price = 0

    # Find all distinct regions in input and update control matrix

    for y in range(len(INPUT)):
        z = 0
        for x in range(len(INPUT[0])):
            if control[y][x]:
                continue

            region = _find_region(INPUT, y, x)

            total_price += _find_area(region) * _find_perimeter(region)

            for ry, rx in region:
                control[ry][rx] = INPUT[ry][rx]

    return total_price

# Part 2 works fine on test cases, but not on the actual input for some reason
def part_2(INPUT):
    control = np.zeros((len(INPUT), len(INPUT[0])), dtype=str)

    total_price = 0

    # Find all distinct regions in input and update control matrix

    for y in range(len(INPUT)):
        z = 0
        for x in range(len(INPUT[0])):
            if control[y][x]:
                continue

            region = _find_region(INPUT, y, x)
            # Price calculated by number of edges rather than edge length
            total_price += _find_area(region) * _find_edges(_find_perimeter(region, True))

            for ry, rx in region:
                control[ry][rx] = INPUT[ry][rx]

    return total_price

def _find_region(_map, start_x, start_y):
    region = set()
    stack = [(start_x, start_y)]

    while stack:
        x, y = stack.pop()
        region.add((x, y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy

            if new_x < 0 or new_x >= len(_map) or new_y < 0 or new_y >= len(_map[0]):
                continue

            if (new_x, new_y) in region:
                continue

            if _map[new_x][new_y] == _map[start_x][start_y]:
                stack.append((new_x, new_y))

    return region

# Find the length of the perimeter of a given region
def _find_perimeter(region, return_perimeter=False):
    perimeter = []

    for x, y in region:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (x + dx, y + dy) not in region:
                perimeter.append((x + dx, y + dy))

    return len(perimeter) if not return_perimeter else perimeter

# Find the total area of a given region
def _find_area(region):
    return len(region)

# Find the total number of edges in a given region
def _find_edges(perimeter, return_edges=False):
    # Given a perimeter, find all edges in the perimeter
    # Find all connected segments in the perimeter
    edges = []
    stack = [pos for pos in perimeter]

    while len(stack) > 0:
        y, x = stack.pop()
        edge = [(y, x)]

        # Check if node has horizontal or neighbors
        if (y, x + 1) in stack or (y, x - 1) in stack:  # Is part of a horizontal edge
            inner_stack = []
            if (y, x + 1) in stack:
                inner_stack.append((y, x + 1))
            if (y, x - 1) in stack:
                inner_stack.append((y, x - 1))

            while len(inner_stack) > 0:
                y, x = inner_stack.pop()
                edge.append((y, x))

                stack.remove((y, x))

                if (y, x + 1) in stack and (y, x + 1) not in edge and (y, x + 1) not in inner_stack:
                    inner_stack.append((y, x + 1))
                if (y, x - 1) in stack and (y, x - 1) not in edge and (y, x - 1) not in inner_stack:
                    inner_stack.append((y, x - 1))


        # Check if node has vertical neighbors
        elif (y + 1, x) in stack or (y - 1, x) in stack:  # Is part of a horizontal edge
            inner_stack = []
            if (y + 1, x) in stack:
                inner_stack.append((y + 1, x))
            if (y - 1, x) in stack:
                inner_stack.append((y - 1, x))

            while len(inner_stack) > 0:
                y, x = inner_stack.pop()
                edge.append((y, x))

                try:
                    stack.remove((y, x))
                except:
                    pass

                if (y + 1, x) in stack and (y + 1, x) not in edge and (y + 1, x) not in inner_stack:
                    inner_stack.append((y + 1, x))
                if (y - 1, x) in stack and (y - 1, x) not in edge and (y - 1, x) not in inner_stack:
                    inner_stack.append((y - 1, x))


        # If no neighbours: edge is a single point
        edges.append(edge)

    return len(edges) if not return_edges else edges


if __name__=="__main__":
    with open("input.txt", "r") as file:
        INPUT = [line.strip() for line in file.readlines()]

    print(part_1(INPUT))
    print(part_2(INPUT))
