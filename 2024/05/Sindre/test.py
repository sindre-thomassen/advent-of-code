import unittest

from main import part_1, part_2

class TestDayFive(unittest.TestCase):
    def test_part1(self):
        _, _, res = part_1('input.test.txt')
        self.assertEqual(res, 143)

    def test_part2(self):
        rules, invalid_cases, _ = part_1('input.test.txt')
        self.assertEqual(part_2(rules, invalid_cases), 123)