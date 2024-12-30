import typing


def run(corruption, n=1024, shape=(71, 71)):
    MAP = [['.' for _ in range(shape[1])] for _ in range(shape[0])]
    for i in range(n):
        x, y = corruption[i]
        try:
            MAP[y][x] = '#'
        except IndexError:
            print(f'IndexError: {x}, {y}', i)
            return None
    # Run A-star to find the shortest path from nw corner to se corner
    start = (0, 0)
    end = (shape[0] - 1, shape[1] - 1)
    path = a_star(MAP, start, end)

    return path

def a_star(MAP, start, end):
    queue: typing.List[Node] = [Node((0, 0), _euclidan_dist((0, 0), end))]
    visited = []

    while len(queue) > 0:
        queue.sort()
        current = queue.pop(0)
        if current.position == end:
            return current

        visited.append(current.position)

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = current.position
            x += dx
            y += dy
            if 0 <= x < len(MAP) and 0 <= y < len(MAP[0]) and MAP[y][x] != '#' and (x, y) not in visited:
                new_node = Node((x, y), _euclidan_dist((x, y), end), current.cost + 1)
                if new_node not in queue:
                    new_node.set_parent(current)
                    queue.append(new_node)

    return None

def _euclidan_dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

class Node:
    def __init__(self, position, distance, cost=0):
        self.parent = None
        self.cost = cost
        self.position = position
        self.distance = distance

    def set_parent(self, parent):
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost or (self.cost == other.cost and self.distance < other.distance)

    def __len__(self):
        if self.parent is None:
            return 0

        return 1 + len(self.parent)

    def __eq__(self, other):
        return self.position == other.position and self.cost == other.cost

def bin_search(data, shape=(71, 71)):
    piv = len(data) // 2
    MIN, MAX = 0, len(data) - 1

    # Find the first n that causes no possible path
    while MIN <= MAX:
        print(MIN, MAX, piv)
        path = run(data, piv, shape)
        if path is None:
            MAX = piv - 1
        else:
            MIN = piv + 1

        piv = (MIN + MAX) // 2

    return data[piv]


if __name__=="__main__":
    with open('input.txt', 'r') as file:
        data = [[int(x) for x in line.strip().split(',')] for line in file]

    path = run(data)
    print(path.cost)
    print(bin_search(data))