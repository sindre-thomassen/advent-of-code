import numpy as np
import re

FILE = "../input.txt"


def is_gear(arr):
	string = ''.join(np.array([list(row)+['.'] for row in arr]).flatten()).replace('*', '.')
	numbers = re.findall("[0-9]+", string)

	return len(numbers) == 2


def remove_fake_gears(arr):
	height, length = arr.shape
	for row in range(height):
		for col in range(length):
			if row == 1 and col == 3:
				continue

			if arr[row, col] == '*':
				arr[row, col] = '.'
	return arr


def find_numbers(arr):
	new_arr = remove_fake_gears(arr.copy())
	is_number = False
	next_number = ""
	numbers = []
	for row in range(len(new_arr)):
		if is_number:
			is_number = False
			numbers.append(int(next_number))
		next_number = ""
		for col in range(len(new_arr[row])):
			if new_arr[row, col] not in '0123456789':
				if is_number:
					numbers.append(int(next_number))
					is_number = False
				
				next_number = ""
				continue

			if new_arr[row, col] in "0123456789":
				next_number += new_arr[row, col]

			if not is_number:	
				for x in range(-1, 2, 1):
					for y in range(-1, 2, 1):
						if x == y == 0:
							continue

						if row+y<0 or row+y >= len(new_arr) or col+x<0 or col+x >= len(new_arr[row]):
							continue

						if new_arr[row+y, col+x] == '*':
							is_number = True
	if is_number:
		numbers.append(int(next_number))
		next_number = ""

	return numbers[0]*numbers[1]


	return 0


with open(FILE) as file:
	lines = file.readlines()

lines = np.array([list(line.strip()) for line in lines])

total = 0

for row in range(len(lines)):
	for col in range(len(lines[row])):
		if lines[row, col] != '*':
			continue

		if not is_gear(lines[
				max(0, row-1):min(len(lines), row+2),
				max(0, col-1):min(len(lines[row]), col+2)
			]):
			continue

		total += find_numbers(lines[
			max(0, row-1):min(len(lines), row+2),
			max(0, col-3):min(len(lines[row]), col+4)
			])

print("Total:", total)