import unittest

from main import part_1, part_2

class TestDay9(unittest.TestCase):
    def setUp(self):
        with open("input.test.txt", "r") as file:
            self.INPUT = [int(x) for x in file.read().strip()]

    def test_part_1(self):
        self.assertEqual(part_1(self.INPUT), 1928)

    def test_part_2(self):
        self.assertEqual(part_2(self.INPUT), 2858)