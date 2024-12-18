import unittest

from main import part_1, part_2

class TestDay8(unittest.TestCase):
    def setUp(self):
        with open("input.test.txt", "r") as file:
            lines = file.readlines()
            self.INPUT = [list(line.strip()) for line in lines]

    def test_part1(self):
        self.assertEqual(part_1(self.INPUT), 14)

    def test_part2(self):
        self.assertEqual(part_2(self.INPUT), 34)
