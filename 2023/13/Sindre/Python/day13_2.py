import numpy as np

FILE = "../input.txt"

with open(FILE) as file:
	areas = []

	line = file.readline()
	while line:
		next_area = []
		while line != "\n" and line != "":
			next_area.append(list(line.strip()))
			line = file.readline()
		areas.append(np.array(next_area))
		line = file.readline()


def find_mirror(arr):
	reflection = False
	smudge = False
	for i in range(1, len(arr)):
		comp = (arr[i-1, :] != arr[i, :]).sum()
		if comp == 0 or comp == 1:
			reflection = True
			if comp == 1:
				smudge = True
			else:
				smudge = False

			for j in range(1, i):
				if i+j >= len(arr):
					break
				
				comp = (arr[i-1-j, :] != arr[i+j, :]).sum()
				
				if comp == 1:
					if smudge:
						reflection = False
						break
					else:
						smudge = True
						continue

				elif comp > 1:
					reflection = False
					break

		if reflection and smudge:
			return i

	return -1


total = 0
for i, arr in enumerate(areas):
	mirror = find_mirror(arr.T)
	if mirror == -1:
		mirror = 100*find_mirror(arr)
	total += mirror


print(total)