def part_1(MAP):
    start, target = None, None

    for i in range(len(MAP)):
        for j in range(len(MAP[0])):
            if MAP[i][j] == 'E':
                target = (i, j)

            if MAP[i][j] == 'S':
                start = (i, j)

            if start and target:
                break

        if start and target:
            break

    velocity = (0, 1)

    return a_star(MAP, start, target, velocity)

def part_2(MAP):
    start, target = None, None

    for i in range(len(MAP)):
        for j in range(len(MAP[0])):
            if MAP[i][j] == 'E':
                target = (i, j)

            if MAP[i][j] == 'S':
                start = (i, j)

            if start and target:
                break

        if start and target:
            break

    velocity = (0, 1)

    return a_star_all(MAP, start, target, velocity)

def a_star(MAP, start, target, start_velocity=(0, 1)):
    stack = [Node(start, velocity=start_velocity)]
    found = False
    visited = {}
    iterations = 0

    while not found and len(stack) > 0:
        node = stack.pop(0)

        visited[node.pos] = node.score

        if node.pos == target:
            print(f"Found solution in {iterations} iterations")
            return node

        iterations += 1

        for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if (dy == node.velocity[0] and dx == -node.velocity[1] and dx != 0) or (dx == node.velocity[1] and dy == -node.velocity[0] and dy != 0):
                continue

            if MAP[node.pos[0]+dy][node.pos[1]+dx] == '#':  # Hit wall
                continue

            next_score = node.score
            if (dy, dx) == node.velocity:
                next_score += 1
            else:
                next_score += 1001

            next_position = (node.pos[0]+dy, node.pos[1]+dx)
            if next_position in visited.keys():
                if visited[next_position] >= node.score:
                    visited[next_position] = node.score
                else:
                    continue

            new_node = Node((node.pos[0]+dy, node.pos[1]+dx), velocity=(dy, dx), score=next_score)
            new_node.set_parent(node)
            stack.append(new_node)

        stack.sort()

def a_star_all(MAP, start, target, start_velocity=(0, 1)):
    stack = [Node(start, velocity=start_velocity)]
    found = False
    visited = {}
    iterations = 0
    paths = []
    LOWEST_SCORE = float('inf')

    while not found and len(stack) > 0:
        node = stack.pop(0)

        visited[(node.pos, node.velocity)] = node.score

        if node.pos == target:
            print(f"Found solution in {iterations} iterations")
            paths.append(node)
            if LOWEST_SCORE > node.score:
                LOWEST_SCORE = node.score
            continue

        iterations += 1

        for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if (dy == node.velocity[0] and dx == -node.velocity[1] and dx != 0) or (dx == node.velocity[1] and dy == -node.velocity[0] and dy != 0):
                continue

            if MAP[node.pos[0]+dy][node.pos[1]+dx] == '#':  # Hit wall
                continue

            next_score = node.score
            if (dy, dx) == node.velocity:
                next_score += 1
            else:
                next_score += 1001

            if next_score > LOWEST_SCORE:
                continue

            next_position = (node.pos[0]+dy, node.pos[1]+dx)
            if (next_position, (dy, dx)) in visited.keys():
                s = visited[(next_position, (dy, dx))]
                if next_score > s:
                    continue

            new_node = Node((node.pos[0]+dy, node.pos[1]+dx), velocity=(dy, dx), score=next_score)
            new_node.set_parent(node)
            stack.append(new_node)

        stack.sort()
    return paths

class Node:
    def __init__(self, pos, velocity=(0, 1), score=0):
        self.score = score
        self.pos = pos
        self.parent = None
        self.velocity = velocity

    def set_parent(self, parent_node):
        self.parent = parent_node

    def __cmp__(self, other):
        if self.score < other.score:
            return -1
        if self.score > other.score:
            return 1
        if self.pos[0] < other.pos[0]:
            return -1
        if self.pos[0] > other.pos[0]:
            return 1
        if self.pos[1] < other.pos[1]:
            return -1
        if self.pos[1] > other.pos[1]:
            return 1
        if self.score == other.score and self.pos == other.pos:
            return 0

    def __gt__(self, other):
        return self.score > other.score

    def __str__(self):
        return f"""
Position:   {self.pos[1]}, {self.pos[0]}
Velocity:   {self.velocity[1]}, {self.velocity[0]}
Score:      {self.score}
        """


if __name__=="__main__":
    with open("input.txt", "r") as file:
        MAP = [list(line.strip()) for line in file.readlines()]

    print(part_1(MAP))
    res = part_2(MAP)

    visits = []

    for node in res:
        visits.append(node.pos)
        while (node := node.parent):
            visits.append(node.pos)

    print(len(set(visits)))