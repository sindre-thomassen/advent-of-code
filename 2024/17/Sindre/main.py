from tqdm import tqdm

class ThreeBitComputer:
    def __init__(self, registers=None):
        if registers is not None:
            self.registers = registers
        else:
            self.registers = {'A': 0, 'B': 0, 'C': 0}

        self.pc = 0
        self.running = False
        self.program = None
        self.output = ''

    def run(self, program, quite=False):
        self.program = program
        self.running = True
        self.output = ''

        while self.running:
            self.step()

        self.output = self.output[:-1]
        if not quite:
            print(self.output)

        self.program = None
        self.pc = 0

    def step(self):
        op = self.program[self.pc]
        value = self.program[self.pc + 1]
        self.pc += 2

        if op == 0:
            self._adv(value)
        elif op == 1:
            self._bxl(value)
        elif op == 2:
            self._bst(value)
        elif op == 3:
            self._jnz(value)
        elif op == 4:
            self._bxc(value)
        elif op == 5:
            self._out(value)
        elif op == 6:
            self._bdv(value)
        elif op == 7:
            self._cdv(value)

        if self.pc >= len(self.program):
            self.running = False

    def _get_value(self, o):
        if o == 7:
            raise Exception('Invalid register')

        if o == 4:
            return self.registers['A']
        elif o == 5:
            return self.registers['B']
        elif o == 6:
            return self.registers['C']
        else:
            return o

    def _adv(self, o):
        value = self._get_value(o)
        self.registers['A'] = self.registers['A'] // (2 ** value)

    def _bxl(self, value):
        self.registers['B'] = self.registers['B'] ^ value

    def _bst(self, o):
        value = self._get_value(o)
        self.registers['B'] = value % 8

    def _jnz(self, value):
        if self.registers['A'] == 0:
            return

        self.pc = value

    def _bxc(self, o):
        self.registers['B'] = self.registers['B'] ^ self.registers['C']

    def _out(self, o):
        self.output += f"{self._get_value(o) % 8},"

    def _bdv(self, o):
        value = self._get_value(o)
        self.registers['B'] = self.registers['A'] // (2 ** value)

    def _cdv(self, o):
        value = self._get_value(o)
        self.registers['C'] = self.registers['A'] // (2 ** value)


def bin_search(program, target):
    # Find the first instance of value in register A to return an output of target length
    registers = {'A': 0, 'B': 0, 'C': 0}
    _min, _max = 0, int(1e20)

    while _min <= _max:
        piv = (_min + _max) // 2
        registers['A'] = piv
        computer = ThreeBitComputer(registers)
        computer.run(program, quite=True)
        if len(computer.output.split(',')) < target:
            _min = piv + 1
        elif len(computer.output.split(',')) >= target:
            _max = piv - 1

    return piv

if __name__ == '__main__':
    with open("input.txt", "r") as file:
        lines = file.readlines()
        registers = dict(zip(['A', 'B', 'C'], [int(line.strip().split(': ')[1]) for line in lines[:3]]))
        program = [int(x) for x in lines[-1].split(': ')[1].split(',')]

    computer = ThreeBitComputer(registers)
    computer.run(program)

    # low = bin_search(program, len(program))
    # high = bin_search(program, len(program)+1)
    #
    # for i in range(low, low + 10):
    #     registers['A'] = i
    #     computer = ThreeBitComputer(registers)
    #     computer.run(program)
