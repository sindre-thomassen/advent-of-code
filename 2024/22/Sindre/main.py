import numpy as np

def generate_number(a):
    N = 16777216

    step_1 = (a ^ (a * 64)) % N
    step_2 = (step_1 ^ (step_1 // 32)) % N
    step_3 = (step_2 ^ (step_2 * 2048)) % N

    return step_3


if __name__=="__main__":
    with open("input.txt", "r") as file:
        a = np.array([int(line.strip()) for line in file.readlines()])

    for i in range(2000):
        a = generate_number(a)

    print(sum(a))