import numpy as np

FILE = "../test_input.txt"

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
	for i in range(1, len(arr)):
		if ''.join(arr[i-1, :]) == ''.join(arr[i, :]):
			reflection = True
			for j in range(0, i):
				if i+j >= len(arr):
					break
				if ''.join(arr[i-1-j, :]) != ''.join(arr[i+j, :]):
					reflection = False
					break
		if reflection:
			return i

	return -1


total = 0
for arr in areas:
	mirror = find_mirror(arr.T)
	if mirror == -1:
		mirror = 100*find_mirror(arr)
	total += mirror


print(total)