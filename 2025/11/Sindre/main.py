TEST = False

with open("./inputs/test.txt" if TEST else "./inputs/input.txt", "r") as f:
    nodes = [line.strip() for line in f.readlines()]


# class Node:
#     def __init__(self, name, size=0, parent=None):
#         self.name = name
#         self.size = size
#         self.parent = parent
#         self.children = []
#
#     def add_child(self, child):
#         self.children.append(child)
#
#     def get_size(self):
#         if self.size > 0:
#             return self.size
#         total_size = 0
#         for child in self.children:
#             total_size += child.get_size()
#         return total_size

node_map = {}
for node in nodes:
    parent, children = node.split(": ")
    node_map[parent] = []
    for child in children.split(" "):
        node_map[parent].append(child)

MAX_ITERATIONS = 1000000000000000000
total = 0
steps = ["you"]
i = 0

while len(steps) > 0 and i < MAX_ITERATIONS:
    i += 1
    current = steps.pop()

    if current == "out":
        total += 1
        continue

    children = node_map.get(current, [])
    for child in children:
        steps.append(child)


print(f"Part 1: {total} ({i} iterations)")


##### PArt 2 #####

# Step 1: simplify map and remove all singletons that only lead to "out" or a single other node
