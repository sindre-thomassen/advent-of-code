import unittest

from main import ThreeBitComputer

class TestComputer(unittest.TestCase):
    def setUp(self):
        with open("input.test.txt", "r") as file:
            lines = file.readlines()
            self.registers = dict(zip(['A', 'B', 'C'], [int(line.strip().split(': ')[1]) for line in lines[:3]]))
            self.program = [int(x) for x in lines[-1].split(': ')[1].split(',')]

    def test_computer(self):
        computer = ThreeBitComputer(self.registers)
        computer.run(self.program)
        self.assertEqual(computer.output, "4,6,3,5,6,3,5,2,1,0")