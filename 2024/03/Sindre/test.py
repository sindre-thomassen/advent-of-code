import unittest

from main import part1, part2

class Day3Tests(unittest.TestCase):

    def setUp(self):
        with open("input.test1.txt", "r") as file:
            self.INPUT_1 = file.read().strip()
        with open("input.test2.txt", "r") as file:
            self.INPUT_2 = file.read().strip()

    def test_part1(self):
        self.assertEqual(161, part1(self.INPUT_1))

    def test_part2(self):
        self.assertEqual(48, part2(self.INPUT_2))
