import unittest

from main import part_1, part_2

class TestDay10(unittest.TestCase):
    def setUp(self):
        with open("input.test.txt", "r") as file:
            self.test_cases = []
            new = True
            case_len = -1

            while (line:=file.readline().strip()):
                if new:
                    new = False
                    case_len = len(line)
                    new_case = []

                if len(line) != case_len:
                    truth = int(line)
                    self.test_cases.append((new_case, truth))
                    new = True
                else:
                    new_case.append(list(line))

        with open("input2.test.txt", "r") as file:
            self.test_cases_2 = []
            new = True
            case_len = -1

            while (line:=file.readline().strip()):
                if new:
                    new = False
                    case_len = len(line)
                    new_case = []

                if len(line) != case_len:
                    truth = int(line)
                    self.test_cases_2.append((new_case, truth))
                    new = True
                else:
                    new_case.append(list(line))

    def test_1_1(self):
        case, truth = self.test_cases[0]
        self.assertEqual(part_1(case), truth)

    def test_1_2(self):
        case, truth = self.test_cases[1]
        self.assertEqual(part_1(case), truth)

    def test_1_3(self):
        case, truth = self.test_cases[2]
        self.assertEqual(part_1(case), truth)

    def test_1_4(self):
        case, truth = self.test_cases[3]
        self.assertEqual(part_1(case), truth)

    def test_2_1(self):
        case, truth = self.test_cases_2[0]
        self.assertEqual(part_2(case), truth)

    def test_2_2(self):
        case, truth = self.test_cases_2[1]
        self.assertEqual(part_2(case), truth)

    def test_2_3(self):
        case, truth = self.test_cases_2[2]
        self.assertEqual(part_2(case), truth)

    def test_2_4(self):
        case, truth = self.test_cases_2[3]
        self.assertEqual(part_2(case), truth)

