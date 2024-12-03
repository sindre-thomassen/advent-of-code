import numpy as np

FILE = "../input.txt"

with open(FILE) as file:
	galaxy = []

	line = file.readline().strip()
	while line:
		galaxy.append(list(line))
		if '#' not in line:
			galaxy.append(list(line))

		line = file.readline().strip()

	galaxy = np.array(galaxy)


new_galaxy = []
for line in list(galaxy.T):
	new_galaxy.append(line)
	if '#' not in line:
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
		total_distance += abs(next_galaxy[0] - gal[0]) + abs(next_galaxy[1] - gal[1])

print("Total distance:", total_distance)