import unittest

from main import build_pattern, run, optimize_pattern

class TestDay19(unittest.TestCase):
    def setUp(self):
        with open("input.test.txt", "r") as file:
            segments = file.readline().strip().split(", ")
            self.pattern = build_pattern(segments)
            print(self.pattern)
            self.pattern = optimize_pattern(segments)
            print(self.pattern)

            file.readline()
            self.strings = file.read().splitlines()

    def test_run(self):
        self.assertEqual(run(self.pattern, self.strings), 6)