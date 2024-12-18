import unittest

from main import part_1

class Test11(unittest.TestCase):
    def setUp(self):
        with open("input.test.txt", "r") as file:
            self.stones = list(map(int, file.readline().split()))

    def test_part_1_1(self):
        self.assertEqual(part_1(self.stones, 0), 2)

    def test_part_1_2(self):
        self.assertEqual(part_1(self.stones, 1), 3)

    def test_part_1_3(self):
        self.assertEqual(part_1(self.stones, 2), 4)

    def test_part_1_4(self):
        self.assertEqual(part_1(self.stones, 3), 5)

    def test_part_1_5(self):
        self.assertEqual(part_1(self.stones, 4), 9)

    def test_part_1_6(self):
        self.assertEqual(part_1(self.stones, 5), 13)

    def test_part_1_7(self):
        self.assertEqual(part_1(self.stones, 6), 22)
