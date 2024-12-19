import unittest

from main import ClawMachine

class TestDay13(unittest.TestCase):
    def setUp(self):
        self.claw_machines = []
        self.fucked_claw_machines = []

        with open("input.test.txt", "r") as file:
            EOF = False
            while not EOF:
                specs = []
                for _ in range(3):
                    line = file.readline().strip()
                    if not line:
                        EOF = True
                        break
                    specs.append(line)

                if EOF:
                    break

                self.claw_machines.append(ClawMachine(specs))
                self.fucked_claw_machines.append(ClawMachine(specs, fucked_units=True))

                line = file.readline()

        self.truths = [280, 0, 200, 0]
        self.fucked_truths = [0, 1, 0, 1]

    def test_clawmachine(self):
        for claw_machine, truth in zip(self.claw_machines, self.truths):
            self.assertEqual(claw_machine.cheapest_win_2(), truth)

    def test_fucked_up_clawmachine(self):
        i = 0
        for claw_machine, truth in zip(self.fucked_claw_machines, self.fucked_truths):
            print(f"Claw machine #{(i := i+1)}", claw_machine)
            if truth == 0:
                self.assertEqual(claw_machine.cheapest_win_2(), truth)
            else:
                self.assertGreater(claw_machine.cheapest_win_2(), 0)
