import numpy as np


REMOVE = set(list('1234567890.'))

def find_numbers(arr):
	signs = set(list(arr.flatten()))
	signs = signs.difference(REMOVE)

	if len(signs) == 0:
		return 0

	num = ""
	for n in arr.flatten():
		if n in "1234567890":
			num += n

	return int(num)

with open("../input.txt") as file:
	lines = file.readlines()

lines = np.array([list(line.strip()) for line in lines])

start = False
total = 0

for row in range(len(lines)):
	for col in range(len(lines[row])):
		if lines[row, col] in "0123456789" and start==False:
			start = col
			continue

		if start != False and (lines[row, col] not in '0123456789' or col == len(lines[row])-1):
			end = col
			
			total += find_numbers(lines[max(0, row-1):min(len(lines), row+2), max(0, start-1):min(len(lines[row]), end+1)])
			start=False

print("Final sum:", total)