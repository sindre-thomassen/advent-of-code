import typing
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class BathroomGuard:
    def __init__(self, position, velocity):
        self._starting_position = np.array(position)
        self._velocity = np.array(velocity)
        self.position = np.array(position)

    def move(self, time=1):
        self.position = self.position + self._velocity * time

    def reset_position(self):
        self.position = self._starting_position

class SecurityProgram:
    def __init__(
            self,
            guards: typing.List[BathroomGuard],
            map_size: typing.Tuple[int, int] = (101, 103)
    ):
        self.guards = guards
        self._map_width, self._map_height = map_size

        self._update_map()

    def move_guards(self, time=1):
        for guard in self.guards:
            guard.move(time)

        self._update_map()

    def _map_init(self):
        self.map = np.array([[0 for _ in range(self._map_width)] for _ in range(self._map_height)])

    def reset_guards(self):
        for guard in self.guards:
            guard.reset_position()

        self._update_map()

    def _update_map(self):
        self._map_init()

        for guard in self.guards:
            x, y = guard.position
            self.map[y % self._map_height][x % self._map_width] += 1

    def print_map(self):
        for row in self.map:
            print(''.join(map(str, row)))

    def calculate_quadrants(self):
        mx = self._map_width // 2
        my = self._map_height // 2

        q1 = self.map[:my, :mx].sum()
        q2 = self.map[:my, mx+1:].sum()
        q3 = self.map[my+1:, :mx].sum()
        q4 = self.map[my+1:, mx+1:].sum()

        return q1, q2, q3, q4

    def get_guard_positions(self):
        return [guard.position % [self._map_width, self._map_height] for guard in self.guards]

if __name__ == '__main__':
    with open('input.txt') as f:
        guards = []
        for line in f.readlines():
            pos, v = line.split()

            guards.append(
                BathroomGuard(
                    list(map(int, pos.replace('p=', '').split(','))),
                    list(map(int, v.replace('v=', '').split(',')))
                )
            )

        system = SecurityProgram(guards)
        system.move_guards(100)
        q1, q2, q3, q4 = system.calculate_quadrants()

        print(q1 * q2 * q3 * q4)

    system.reset_guards()

    cur = float('inf')
    unchanged = 0
    s = 0
    i = 0

    while unchanged < 5000:
        positions = np.array(system.get_guard_positions())
        if np.var(positions) < cur:
            cur = np.var(positions)
            unchanged = 0
            s = i
        else:
            unchanged += 1

        system.move_guards()
        i += 1

    print(unchanged, cur, f"Wait for {s} seconds")