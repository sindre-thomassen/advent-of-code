import unittest
import numpy as np

from main import generate_number

class TestDay22(unittest.TestCase):
    def setUp(self):
        with open("input.test.txt", "r") as file:
            self.numbers = np.array([int(line.strip()) for line in file.readlines()])

    def test_part_1(self):
        res = self.numbers.copy()

        for i in range(2000):
            self.numbers = generate_number(self.numbers)

        self.assertEqual(sum(self.numbers), 37327623)