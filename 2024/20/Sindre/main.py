import time

import numpy as np


def a_star(MAP, start, target, visited=set(), max_cost=None):
    queue = [Node(start, _euclidean_distance(start, target))]

    while queue:
        node = queue.pop(0)
        if node.position == target:
            return node

        # Early stopping if cost is too high
        if max_cost is not None and node.cost > max_cost:
            return None

        visited.add(node.position)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = node.position
            new_pos = x + dx, y + dy
            if new_pos in visited or new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(MAP[0]) or new_pos[1] >= len(MAP):
                continue
            if MAP[new_pos[1]][new_pos[0]] == "#":
                continue
            new_node = Node(new_pos, _euclidean_distance(new_pos, target), node.cost + 1, node)
            if new_node not in queue:
                queue.append(new_node)


    return None

def _euclidean_distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

class Node:
    def __init__(self, pos, distance, cost=0, parent=None):
        self.position = pos
        self.cost = cost
        self.parent = parent
        self.distance = distance

    def __lt__(self, other):
        return self.cost < other.cost or self.cost == other.cost and self.distance < other.distance

    def __eq__(self, other):
        return self.position == other.position and self.cost == other.cost

    def __len__(self):
        if self.parent is None:
            return 0
        return 1 + len(self.parent)


if __name__=='__main__':
    with open("input.txt", "r") as f:
        MAP = [list(line.strip()) for line in f.readlines()]

    start, target = None, None

    for y in range(len(MAP)):
        for x in range(len(MAP[y])):
            if MAP[y][x] == "S":
                start = x, y
                MAP[y][x] = "."
            if MAP[y][x] == "E":
                target = x, y
                MAP[y][x] = "."

    node = a_star(MAP, start, target)
    legit_fastest = node.cost
    cheating_costs = []
    print("Legit fastest path:", legit_fastest)
    i = 0

    t = time.time()

    while (node := node.parent) is not None:
        if i % 250 == 0:
            print(f"{i}/{legit_fastest} ({time.time()-t:.2f}s)")
            t = time.time()

        i += 1
        neighbours = [(node.position[0] + dx, node.position[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

        # Cheat and start inside a wall. If path is shorter than originally, cheat has worked
        for neighbour in neighbours:
            visited = set([node.position])
            if neighbour[0] < 0 or neighbour[1] < 0 or neighbour[0] >= len(MAP[0]) or neighbour[1] >= len(MAP):
                continue
            if MAP[neighbour[1]][neighbour[0]] == ".":
                continue

            max_cost = legit_fastest - node.cost - 1

            new_path = a_star(MAP, neighbour, target, visited, max_cost)
            if new_path is not None:
                cost = new_path.cost
            else:
                continue

            if (node.cost + cost + 1) < legit_fastest:
                cheating_costs.append(legit_fastest - (node.cost + cost + 1))

    print(sum(np.array(cheating_costs) >= 100))