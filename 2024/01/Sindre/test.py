import unittest

module = __import__("01.Sindre.main")

class FirstOfDecemberTest(unittest.TestCase):

    def setUp(self):
        file = open("01/Sindre/input.test.txt", "r")
        self.test_input = [[int(x) for x in line.split()] for line in file.readlines()]
        file.close()

    def test_part1(self):
        self.assertEqual(module.Sindre.main.part1(self.test_input), 11)

    def test_part2(self):
        self.assertEqual(module.Sindre.main.part2(self.test_input), 31)