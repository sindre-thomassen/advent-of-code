def part_1(MAP):
    sim = GuardSimulator(MAP)
    return sim.simulate()


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
        while self.take_step() != -1:
            pass

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
            self.MAP[self.pos[1]][self.pos[0]] = "X"
            return -1

        # Has hit a wall
        if self.MAP[next_pos[1]][next_pos[0]] == "#":
            self._turn_right()
            return 0

        # Has walked
        # Update map and new position
        self.MAP[self.pos[1]][self.pos[0]] = "X"
        self.pos = next_pos

        return 1

    def calculate_visited_cells(self):
        visited_cells = 0
        for y in range(len(self.MAP)):
            for x in range(len(self.MAP[0])):
                if self.MAP[y][x] == "X":
                    visited_cells += 1

        return visited_cells

    def _turn_right(self):
        self._velocity_index = (self._velocity_index + 1) % 4
        self.velocity = self._velocities[self._velocity_index]

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        MAP = [list(line.strip()) for line in file.readlines()]

    print(part_1(MAP))