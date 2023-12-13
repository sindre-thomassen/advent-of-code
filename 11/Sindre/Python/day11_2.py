import numpy as np

FILE = "../input.txt"

with open(FILE) as file:
	galaxy = []

	line = file.readline().strip()
	while line:
		galaxy.append(list(line))
		if '#' not in line:
			for i in range(500):
				galaxy.append(list(line))

		line = file.readline().strip()

	galaxy = np.array(galaxy)


new_galaxy = []
for line in list(galaxy.T):
	new_galaxy.append(line)
	if '#' not in line:
		for i in range(500):
			new_galaxy.append(line)

galaxy = np.array(new_galaxy).T

galaxies = []
total_distance = 0

for row in range(len(galaxy)):
	for col in range(len(galaxy[0])):
		if galaxy[row, col] == '#':
			galaxies.append((row, col))

while len(galaxies) > 0:
	next_galaxy = galaxies.pop(0)

	for gal in galaxies:
		distance = abs(next_galaxy[0] - gal[0]) + abs(next_galaxy[1] - gal[1])
		if distance >= 500:
			DISTANCE = distance % 500
			DISTANCE += (distance // 500) * (1000000-1)
			distance = DISTANCE

		total_distance += distance

print("Total distance:", total_distance)