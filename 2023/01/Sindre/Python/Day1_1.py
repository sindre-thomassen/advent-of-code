import re

INPUT_FILE = "../input.txt"
TEST_INPUT_FILE = "../test_input.txt"

with open(INPUT_FILE) as file:
	lines = file.readlines()

s = 0
for line in lines:
	numbers = re.findall("[\d]", line)
	number = int(f"{numbers[0]}{numbers[-1]}")

	s += number

print(f"Calibration number: {s}")