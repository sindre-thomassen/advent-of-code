import unittest

from main import part_1, part_2

class TestDay7(unittest.TestCase):
    def setUp(self):
        with open("input.test.txt", "r") as file:
            lines = [line.strip().split(':') for line in file.readlines()]
            self.INPUT = [
                (int(line[0]), [int(x) for x in line[1].strip().split(' ')]) for line in lines
            ]

    def test_part1(self):
        self.assertEqual(part_1(self.INPUT), 3749)

    def test_part2(self):
        self.assertEqual(part_2(self.INPUT), 11387)