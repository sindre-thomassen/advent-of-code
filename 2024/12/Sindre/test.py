import unittest

from main import part_1, part_2

class TestDay12(unittest.TestCase):
    def setUp(self):
        with open("input.test.txt", "r") as file:
            self.INPUT = [line.strip() for line in file.readlines()]

    def test_part_1_1(self):
        self.assertEqual(part_1(self.INPUT), 1930)

    def test_part_1_2(self):
        tmp_input = [
            "AAAA",
            "BBCD",
            "BBCC",
            "EEEC"
        ]

        self.assertEqual(part_1(tmp_input), 140)

    def test_part_1_3(self):
        tmp_input = [
            "OOOOO",
            "OXOXO",
            "OOOOO",
            "OXOXO",
            "OOOOO"
        ]

        self.assertEqual(part_1(tmp_input), 772)

    def test_part_2_1(self):
        tmp_input = [
            "AAAA",
            "BBCD",
            "BBCC",
            "EEEC"
        ]
        self.assertEqual(part_2(self.INPUT), 1206)

    def test_part_2_2(self):
        tmp_input = [
            "EEEEE",
            "EXXXX",
            "EEEEE",
            "EXXXX",
            "EEEEE"
        ]
        self.assertEqual(part_2(tmp_input), 236)

    def test_part_2_3(self):
        tmp_input = [
            "AAAAAA",
            "AAABBA",
            "AAABBA",
            "ABBAAA",
            "ABBAAA",
            "AAAAAA"
        ]
        self.assertEqual(part_2(tmp_input), 368)

    def test_part_2_4(self):
        tmp_input = [
            "OOOOO",
            "OXOXO",
            "OOOOO",
            "OXOXO",
            "OOOOO"
        ]

        self.assertEqual(part_2(tmp_input), 436)