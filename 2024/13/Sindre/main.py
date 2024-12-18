class ClawMachine:
    def __init__(self, specs, fucked_units=False):
        self.setup_clawmachine(specs, fucked_units)

    def setup_clawmachine(self, specs, fucked_units):
        self._specs = specs
        self.btn_a = [int(x.split('+')[1]) for x in specs[0].split(': ')[1].split(', ')]
        self.btn_b = [int(x.split('+')[1]) for x in specs[1].split(': ')[1].split(', ')]

        self.price_a = 3
        self.price_b = 1

        # If prize units are fucked, we need to adjust the prize location
        self.fucked_units = fucked_units
        self.prize_location = [int(x.split('=')[1]) + (10000000000000 if fucked_units else 0) for x in specs[2].split(': ')[1].split(', ')]

        self.max_b_press = min([self.prize_location[0] // self.btn_b[0], self.prize_location[1] // self.btn_b[1]])

        self.winable = self._win_is_possible()

    # Check whether or not the prize can be won with any combination of button presses
    def _win_is_possible(self):
        # Want to use button B as much as possible
        for i in range(self.max_b_press, 0, -1):
            if self.btn_b[0] * i > self.prize_location[0] or self.btn_b[1] * i > self.prize_location[1]:
                continue

            bdx, bdy = self.btn_b[0] * i, self.btn_b[1] * i
            remainder = [self.prize_location[0] - bdx, self.prize_location[1] - bdy]

            if remainder[0] % self.btn_a[0] == 0 and remainder[1] % self.btn_a[1] == 0 and remainder[0] // self.btn_a[0] == remainder[1] // self.btn_a[1]:
                return True
        return False

    def cheapest_win(self):
        # if not self.winable:
        #     return 0

        # Want to use button A as much as possible
        for i in range(self.max_b_press, 0, -1):
            if self.btn_b[0] * i > self.prize_location[0] or self.btn_b[1] * i > self.prize_location[1]:
                continue

            bdx, bdy = self.btn_b[0] * i, self.btn_b[1] * i
            remainder = [self.prize_location[0] - bdx, self.prize_location[1] - bdy]

            if remainder[0] % self.btn_a[0] == 0 and remainder[1] % self.btn_a[1] == 0 and remainder[0] / self.btn_a[0] == remainder[1] / self.btn_a[1]:
                return self.price_b * i + self.price_a * (remainder[0] // self.btn_a[0])

        return 0

    def __str__(self):
        string = f"""
        Claw Machine Specifications:
        Button A: X+{self.btn_a[0]}, Y+{self.btn_a[1]}
        Button B: X+{self.btn_b[0]}, Y+{self.btn_b[1]}
        Prize Location: X={self.prize_location[0]}, Y={self.prize_location[1]}
        Winable: {self.winable}
        """
        if self.winable:
            string += f"Cheapest Win: {self.cheapest_win()}"
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
            total_cost += claw_machine.cheapest_win()

            line = file.readline()

    print(total_cost)