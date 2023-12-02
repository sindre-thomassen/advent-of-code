from functools import reduce


with open("../input.txt") as file:
	lines = list(map(lambda x: x.strip(), file.readlines()))

total = 0

for line in lines:
	mins = {
		'blue': 0,
		'red': 0,
		'green': 0
	}
	game_index, game_results = line.split(':')

	for res in game_results.split(';'):
		for subset in res.split(', '):
			n, color = subset.strip().split(' ')
			mins[color] = max(mins[color], int(n))

	total += reduce(lambda x, y: x*y, mins.values(), 1)

print(total)