import numpy as np

class ClawMachine:
    def __init__(self, specs, fucked_units=False):
        self.setup_clawmachine(specs, fucked_units)

    def setup_clawmachine(self, specs, fucked_units):
        self._specs = specs
        self.btn_a = np.array([int(x.split('+')[1]) for x in specs[0].split(': ')[1].split(', ')])
        self.btn_b = np.array([int(x.split('+')[1]) for x in specs[1].split(': ')[1].split(', ')])

        self.price_a = 3
        self.price_b = 1

        # If prize units are fucked, we need to adjust the prize location
        self.fucked_units = fucked_units
        self.prize_location = np.array([int(x.split('=')[1]) + (10000000000000 if fucked_units else 0) for x in specs[2].split(': ')[1].split(', ')])

    def cheapest_win(self):
        # If any combination of button presses can win, there should be an x so that -> (prize_location - button_a * x) % button_b == 0
        start = self.prize_location % self.btn_b

        # If we reach a point where the modulo is 0, we have found a solution
        # If we reach a point where the modulo is the same as the start, we have no solution
        i = 1
        solution = False
        loop = False

        while not solution and not loop:
            if i % 1000 == 0:
                print(i)

            if ((self.prize_location - self.btn_a * i) % self.btn_b == 0).all():
                b_presses = (self.prize_location - self.btn_a * i) // self.btn_b
                if b_presses[0] != b_presses[1]:
                    print("False positive. Keep going")
                else:
                    solution = True
                    break

            if ((self.prize_location - self.btn_a * i) % self.btn_b == start).all():
                loop = True
                break

            i += 1

        if solution:
            a_presses = i
            b_presses = (self.prize_location - self.btn_a * i) // self.btn_b

            return a_presses * self.price_a + b_presses[0] * self.price_b

        else:
            print("No solution")
            return 0

    def cheapest_win_2(self):
        # Solve equations to find intersection of (0, 0) + btn a and prize location - btn b
        s = (self.prize_location[1]*self.btn_b[0] - self.prize_location[0]*self.btn_b[1]) / (self.btn_a[1]*self.btn_b[0] - self.btn_a[0]*self.btn_b[1])
        t = (self.prize_location[0] - self.btn_a[0]*s) / self.btn_b[0]

        if (self.prize_location - self.btn_a * s - self.btn_b * t == 0).all() and int(s) == s and int(t) == t:
            return self.price_a * s + self.price_b * t
        else:
            return 0

    def __str__(self):
        string = f"""
        Claw Machine Specifications:
        Button A: X+{self.btn_a[0]}, Y+{self.btn_a[1]}
        Button B: X+{self.btn_b[0]}, Y+{self.btn_b[1]}
        Prize Location: X={self.prize_location[0]}, Y={self.prize_location[1]}"""
        return string


if __name__=="__main__":
    with open("input.txt", "r") as file:
        total_cost = 0
        EOF = False
        i = 0
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

            i += 1

            claw_machine = ClawMachine(specs, fucked_units=True)
            total_cost += claw_machine.cheapest_win_2()

            line = file.readline()

    print(total_cost)