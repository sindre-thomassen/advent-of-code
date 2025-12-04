import numpy as np

TEST = False


MAP = []

with open("./inputs/test.txt" if TEST else "./inputs/input.txt", "r") as file:
	while (line:=file.readline().strip()):
		MAP.append(list(line))

MAP = np.array(MAP)

n_rows, n_cols = MAP.shape
count = 0





##### Part 1 #####

for row in range(n_rows):
	for col in range(n_cols):
		if MAP[row, col] == '@': # Cell is roll of paper
			slice = MAP[
				max(row-1, 0):min(n_rows-1, row+1)+1,
				max(col-1, 0):min(n_cols-1, col+1)+1
			].copy()


			if row == 0:
				if col == 0:
					slice[0, 0] = 'X'
				else:
					slice[0, 1] = 'X'
			else:
				if col == 0:
					slice[1, 0] = 'X'
				else:
					slice[1, 1] = 'X'

			count += int((slice=='@').sum()<4)

print()
print(f"Part 1: {count}")
print()




##### Part 2 #####

changed = True
old_count = -1
count = 0
iterations = 0

while count != old_count:
	old_count = count
	iterations += 1
	print(f"Iteration {iterations}")

	for row in range(n_rows):
		for col in range(n_cols):
			if MAP[row, col] == '@': # Cell is roll of paper
				slice = MAP[
					max(row-1, 0):min(n_rows-1, row+1)+1,
					max(col-1, 0):min(n_cols-1, col+1)+1
				]

				removeable = (slice=='@').sum()<5	# Account for roll being processed

				if removeable:
					if row == 0:
						if col == 0:
							slice[0, 0] = '.'
						else:
							slice[0, 1] = '.'
					else:
						if col == 0:
							slice[1, 0] = '.'
						else:
							slice[1, 1] = '.'
					
					count += 1

print()
print(f"Part 2: {count}")
print()
