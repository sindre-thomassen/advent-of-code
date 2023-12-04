import re

FILE = "../input.txt"

with open(FILE) as file:
	lines = file.readlines()


def calc_points(guesses, truth):
	correct_numbers = set(guesses).intersection(truth)
	if len(correct_numbers) == 0:
		return 0

	return 2**(len(correct_numbers)-1)

total_score = 0
for line in lines:
	line = line.split(':')[1].strip()
	guesses, truth = line.split(' | ')

	guesses = [int(x) for x in re.findall("[0-9]+", guesses)]
	truth = [int(x) for x in re.findall("[0-9]+", truth)]

	total_score += calc_points(guesses, truth)

print("Total score:", total_score)