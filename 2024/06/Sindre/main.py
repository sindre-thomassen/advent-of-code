def part_1(MAP):
    new_map = [[x for x in row] for row in MAP]
    sim = GuardSimulator(new_map)
    res = sim.simulate()
    return res, new_map

def part_2(MAP, ref_map):
    possible_loops = 0
    # Loop through all alternative maps and look for infinite loops
    for y in range(len(MAP)):
        for x in range(len(MAP[0])):
            if type(ref_map[y][x]) != list or MAP[y][x] == "^":
                continue

            new_map = [[x for x in row] for row in MAP]
            new_map[y][x] = "#"

            sim = GuardSimulator(new_map)
            if sim.simulate() == -1:
                possible_loops += 1

    return possible_loops

class GuardSimulator:
    def __init__(self, MAP):
        self.MAP = MAP
        self.pos = self.__find_start_position()
        self.velocity = (0, -1)

        self._velocity_index = 0
        self._velocities = [
            (0, -1),
            (1, 0),
            (0, 1),
            (-1, 0)
        ]

    def simulate(self):
        while (status := self.take_step()) != -1:
            if status == -2:
                return -1  # Infinite loop detected, should not happen

        return self.calculate_visited_cells()

    def __find_start_position(self):
        for y, row in enumerate(self.MAP):
            for x, cell in enumerate(row):
                if cell == "^":
                    return x, y

    def take_step(self):
        next_pos = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1])

        # Has exited the map
        if next_pos[0] < 0 or next_pos[0] >= len(self.MAP[0]) or next_pos[1] < 0 or next_pos[1] >= len(self.MAP):
            update = self._update_map()
            if update == -1:
                return -2
            return -1

        # Has hit a wall
        if self.MAP[next_pos[1]][next_pos[0]] == "#":
            self._turn_right()
            self._update_map(turn=True)
            return 0

        # Has walked
        # Update map and new position
        update = self._update_map()
        if update == -1:
            return -2

        self.pos = next_pos

        return 1

    def _update_map(self, turn=False):
        if turn:
            return

        if type(self.MAP[self.pos[1]][self.pos[0]]) != list:
            self.MAP[self.pos[1]][self.pos[0]] = [self.velocity]
        else:
            if self.velocity in self.MAP[self.pos[1]][self.pos[0]]:
                return -1  # Infinite loop detected

            self.MAP[self.pos[1]][self.pos[0]].append(self.velocity)

    def calculate_visited_cells(self):
        visited_cells = 0
        for y in range(len(self.MAP)):
            for x in range(len(self.MAP[0])):
                if self.MAP[y][x] not in ["#", "."]:
                    visited_cells += 1

        return visited_cells

    def _turn_right(self):
        self._velocity_index = (self._velocity_index + 1) % 4
        self.velocity = self._velocities[self._velocity_index]

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        MAP = [list(line.strip()) for line in file.readlines()]

    res, sim = part_1(MAP)
    print(res)
    print(part_2(MAP, sim))