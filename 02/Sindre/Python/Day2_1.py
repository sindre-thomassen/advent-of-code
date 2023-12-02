with open("../input.txt") as file:
	lines = list(map(lambda x: x.strip(), file.readlines()))

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

maxs = {
	'blue': MAX_BLUE,
	'red': MAX_RED,
	'green': MAX_GREEN
}

total = 0

for line in lines:
	game_index, game_results = line.split(':')

	possible = True
	for res in game_results.split(';'):
		for subset in res.split(', '):
			n, color = subset.strip().split(' ')
			if maxs[color] < int(n):
				possible = False
				break
		if not possible:
			break

	if possible:
		total += int(game_index.split(' ')[1])

print(total)