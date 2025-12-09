from functools import reduce


class Node:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.connections = []
        self.traversed = False  # For traversal algorithms

    def euclidean_distance_3d(self, other) -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5

    # Add two way connection between nodes
    def append_connection(self, other):
        if other not in self.connections:
            self.connections.append(other)
        if self not in other.connections:
            other.connections.append(self)

    def calculate_size(self, log_traversed=False) -> int:
        visited = set()
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)

            if log_traversed:
                node.traversed = True

            size = 1
            for neighbor in node.connections:
                size += dfs(neighbor)
            return size

        if log_traversed:
            self.traversed = True

        return dfs(self)

    def set_visited(self, visited: bool):
        self.traversed = visited

    def __sub__(self, other):
        return self.euclidean_distance_3d(other)

    def __repr__(self):
        return f"Node({self.x}, {self.y}, {self.z}, connections={len(self.connections)}, traversed={self.traversed})"


TEST = False

with (open("./inputs/test.txt" if TEST else "./inputs/input.txt", "r") as f):
    nodes = []
    while (line:= f.readline().strip()):
        nodes.append(Node(*map(int, line.split(","))))


# Iterate through all combinations of nodes and calculate distances. Sort by shortest distances, and pair together the top X number of node combinations.
combinations = []
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        dist = nodes[i] - nodes[j]
        # Save (distance, node1_i, node2_j) only indices for better memory usage
        combinations.append((dist, i, j))

combinations = sorted(combinations, key=lambda x: x[0])
for _, i, j in combinations[:(10 if TEST else 1000)]:
    nodes[i].append_connection(nodes[j])

##### Part 1 #####

sizes = []
for node in nodes:
    if not node.traversed:
        sizes.append(node.calculate_size(log_traversed=True))

print(reduce(lambda x, y: x * y, sorted(sizes, reverse=True)[:3]))



##### Part 2 #####
# Connect all nodes into one large graph
while (current_size:=nodes[0].calculate_size()) < len(nodes) and len(combinations) > 0:
    _, i, j = combinations.pop(0)
    nodes[i].append_connection(nodes[j])

    # print("Current size:", current_size)

print(nodes[0].calculate_size())
# Answer is x coordinate of last two nodes connected multiplied together
print(f"Last two nodes connected: {nodes[i]}, {nodes[j]} with x coordinates {nodes[i].x}, {nodes[j].x} ({nodes[i].x * nodes[j].x})")
