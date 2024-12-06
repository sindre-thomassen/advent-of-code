import unittest

from main import part_1

class TestDay6(unittest.TestCase):
    def setUp(self):
        with open("input.test.txt", "r") as file:
            self.MAP = [list(line.strip()) for line in file.readlines()]

    def test_part_1(self):
        self.assertEqual(part_1(self.MAP), 41)
