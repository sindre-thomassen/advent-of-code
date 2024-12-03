import re

FILE = "../input.txt"

with open(FILE) as file:
	lines = file.readlines()


games = []
for line in lines:
	game = line.split(':')[1].strip()
	guesses, truth = game.split(' | ')

	guesses = [int(x) for x in re.findall("[0-9]+", guesses)]
	truth = [int(x) for x in re.findall("[0-9]+", truth)]

	games.append((guesses, truth))

record = dict([(x+1, 1) for x in range(len(games))])
total = 0

def calc_points(guesses, truth):
	correct_numbers = set(guesses).intersection(truth)
	if len(correct_numbers) == 0:
		return 0

	return len(correct_numbers)


for i in range(len(games)):
	total += 1

	game = games[i]
	score = calc_points(*game)

	for next_ticket in range(i+1, i+1+score):
		record[next_ticket+1] += record[i+1]


print("Total number of tickets:", sum(record.values()))