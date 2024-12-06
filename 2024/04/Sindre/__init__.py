import numpy as np

with open("input.txt", "r") as file:
    _INPUT = file.readlines()
    _INPUT = np.array([list(x.strip()) for x in _INPUT])

with open("input.test.txt", "r") as file:
    _INPUT_TEST = file.readlines()
    _INPUT_TEST = np.array([list(x.strip()) for x in _INPUT_TEST])
