import re


def gen_num(numbers):
	n1, n2 = numbers[0], numbers[-1]

	if len(n1) > 1:
		n1 = NUMBERS[n1]

	if len(n2) > 1:
		n2 = NUMBERS[n2]

	return int(f"{n1}{n2}")


INPUT_FILE = "../input.txt"
TEST_INPUT_FILE = "../test_input.txt"

NUMBERS = {
	"one": "1",
	"two": "2",
	"three": "3",
	"four": "4",
	"five": "5",
	"six": "6",
	"seven": "7",
	"eight": "8",
	"nine": "9",
	"zero": "0"
}
PATTERN = "(?=(" + '|'.join(['[\d]'] + list(NUMBERS.keys())) + "))"


with open(INPUT_FILE) as file:
	lines = file.readlines()

s = 0
for line in lines:
	numbers = re.findall(PATTERN, line)
	number = gen_num(numbers)
	
	s += number

print(f"Calibration number: {s}")