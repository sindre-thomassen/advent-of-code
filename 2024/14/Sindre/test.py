import unittest
from functools import reduce

from main import BathroomGuard, SecurityProgram

class TestDay14(unittest.TestCase):
    def setUp(self):
        with open('input.test.txt') as f:
            guards = []
            for line in f.readlines():
                pos, v = line.split()

                guards.append(
                    BathroomGuard(
                        list(map(int, pos.replace('p=', '').split(','))),
                        list(map(int, v.replace('v=', '').split(',')))
                    )
                )

            self.system = SecurityProgram(guards, (11, 7))

    def test_part_1(self):
        self.system.move_guards(100)

        qs = self.system.calculate_quadrants()

        self.assertEqual(reduce(lambda x, y: x * y, qs, 1), 12)
        self.system.move_guards(-100)