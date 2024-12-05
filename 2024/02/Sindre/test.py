import unittest

from main import part1, part2

class Day2Tests(unittest.TestCase):

    def setUp(self):
        with open("input.test.txt", "r") as file:
            self.INPUT = [[int(x) for x in line.split()] for line in file.readlines()]

    def test_part1(self):
        self.assertEqual(2, part1(self.INPUT))

    def test_part2(self):
        self.assertEqual(4, part2(self.INPUT))
