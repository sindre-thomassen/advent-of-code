import unittest
import numpy as np

from Sindre import _INPUT_TEST
from Sindre.directions import check_horizontally, check_vertically, check_diagonally
from Sindre.main import part1, part2


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.INPUT = _INPUT_TEST
        self.Xs = np.argwhere(self.INPUT == "X")

    def test_horizontally(self):
        score = 0
        for y, x in self.Xs:
            score += check_horizontally(self.INPUT, x, y)

        self.assertEqual(score, 5)

    def test_vertically(self):
        score = 0
        for y, x in self.Xs:
            score += check_vertically(self.INPUT, x, y)

        self.assertEqual(score, 3)

    def test_diagonally(self):
        score = 0
        for y, x in self.Xs:
            score += check_diagonally(self.INPUT, x, y)

        self.assertEqual(score, 10)

    def test_part1(self):
        self.assertEqual(part1(self.INPUT), 18)

    def test_part2(self):
        self.assertEqual(part2(self.INPUT), 9)