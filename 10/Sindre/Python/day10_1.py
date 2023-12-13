FILE = "../input.txt"

with open(FILE) as file:
	lines = [list(line.strip()) for line in file.readlines()]


queue = []
for i in range(len(lines)):
	for j in range(len(lines[0])):
		if lines[i][j] == "S":
			queue = [(i, j)]
			break

	if len(queue) > 0:
		break


visited = []
while len(queue) > 0:
	pos = queue.pop(0)
	visited.append(pos)

	row, col = pos
	current_pipe = lines[row][col]

	# Check right
	if current_pipe in ["S", "L", "F", "-"]:
		new_col = col + 1
		if new_col < len(lines[0]):
			if lines[row][new_col] in ["-", "J", "7"] and (row, new_col) not in visited and (row, new_col) not in queue:
				queue.append((row, new_col))

	# Check down
	if current_pipe in ["S", "7", "F", "|"]:
		new_row = row + 1
		if new_row < len(lines):
			if lines[new_row][col] in ["|", "L", "J"] and (new_row, col) not in visited and (new_row, col) not in queue:
				queue.append((new_row, col))
	
	# Check left
	if current_pipe in ["S", "J", "7", "-"]:
		new_col = col - 1
		if new_col >= 0:
			if lines[row][new_col] in ["-", "L", "F"] and (row, new_col) not in visited and (row, new_col) not in queue:
				queue.append((row, new_col))

	# Check up
	if current_pipe in ["S", "L", "J", "|"]:
		new_row = row - 1
		if new_row >= 0:
			if lines[new_row][col] in ["|", "7", "F"] and (new_row, col) not in visited and (new_row, col) not in queue:
				queue.append((new_row, col))

print(len(visited)//2)
