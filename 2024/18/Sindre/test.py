import unittest

from main import run
from main import bin_search

class TestDay18(unittest.TestCase):
    def setUp(self):
        with open('input.test.txt', 'r') as file:
            self.data = [[int(x) for x in line.strip().split(',')] for line in file]

    def test_run(self):
        path = run(self.data, 12, (7, 7))
        self.assertEqual(path.cost, 22)

    def test_bin_search(self):
        self.assertEqual(bin_search(self.data, (7, 7)), [6, 1])