import numpy as np
import time as t


FILE = "../input.txt"
with open(FILE) as file:
	lines = np.array([list(line.strip()) for line in file.readlines()])


def move_rocks(row):
	current_index = None
	for i in range(len(row)):
		if current_index == None and row[i] == '.':
			current_index = i
			continue

		if row[i] == '#':
			current_index = None
			continue

		if row[i] == 'O' and current_index != None:
			row[current_index] = 'O'
			row[i] = '.'

			if row[current_index+1] == '.':
				current_index += 1

	return row


def main_process():
	global lines

	for col in range(len(lines[0])):
		lines[:, col] = move_rocks(lines[:, col])

# for n in [10, 20, 40, 100, 1000]:
	# start = t.time()
	# for _ in range(n):
main_process()
	# print(f"{n} iterations: {t.time()-start} seconds")


total = 0
for i in range(len(lines)):
	total += (len(lines) - i)*(lines[i]=='O').sum()

print(total)