from tqdm import tqdm

MAX=100


def process_turn(direction, n, current=50):
	if direction == 'L':
		current -= n
	elif direction == 'R':
		current += n

	return current%MAX


def process_turn_alt(direction, n, current=50):
	# Count number of passes
	score = n // MAX # Full circles
	n %= MAX

	# Rotate and count if passing 0
	if direction == "L":
		# if current == 0:
		# 	score += 1
		current -= n
		if current < 0:
			score += 1
	elif direction == "R":
		if current == 0:
			score += 1
		current += n
		if current > MAX:
			score += 1

	return current % MAX, score


# with open("inputs/input.txt", "r") as file:
with open("inputs/input.txt", "r") as file:
	lines = [(line[0], int(line[1:])) for line in file.readlines()]


# Part 1

score = 0
next_pos = 50
for direction, n in tqdm(lines):
	next_pos = process_turn(direction, n, next_pos)
	if next_pos == 0:
		score += 1

print(f"Answer to part 1: {score}")


# Part 2

score = 0
next_pos = 50
for direction, n in tqdm(lines):
	print(next_pos, score)
	
	next_pos, bonus = process_turn_alt(direction, n, next_pos)
	score += bonus
print(next_pos, score)


print(f"Answer to part 2: {score}")