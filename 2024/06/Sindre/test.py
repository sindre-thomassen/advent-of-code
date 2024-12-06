import unittest

from main import part_1, part_2

class TestDay6(unittest.TestCase):
    def setUp(self):
        with open("input.test.txt", "r") as file:
            self.MAP = [list(line.strip()) for line in file.readlines()]

    def test_part_1(self):
        res, _ = part_1(self.MAP)
        self.assertEqual(res, 41)

    def test_part_2(self):
        res, ref = part_1(self.MAP)
        self.assertEqual(part_2(self.MAP, ref), 6)