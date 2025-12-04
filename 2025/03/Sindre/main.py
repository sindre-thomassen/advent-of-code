##### Part 1 ######



TEST = False


with open("inputs/test.txt" if TEST else "inputs/input.txt", "r") as file:
	lines = [line.strip() for line in file.readlines()]

# joltages = []

# for line in lines:
# 	tenner_place = 0
# 	singles_place = 0

# 	for n in line[:-1]:
# 		if int(n) > tenner_place:
# 			tenner_place = int(n)
# 			singles_place = 0
# 		elif int(n) > singles_place:
# 			singles_place = int(n)

# 	if int(line[-1])>singles_place:
# 		singles_place = int(line[-1])

# 	joltages.append(tenner_place*10 + singles_place)


# print(joltages, sum(joltages))





##### Part 2 #####

N = 12 # Number of batteries to activate
joltages = []

for line in lines:
	print(line)
	piv = 0
	digits = []

	for n in range(N):
		next_digit = -1

		##### Loop through all candidates and find the maximum numeber from left digit to rightmost digit
		segment = line[piv:len(line)-(N-1-n)]
		best_index = -1
		for i, c in enumerate(segment):
			if int(c) > next_digit:
				next_digit = int(c)
				best_index = piv + i
		
		piv = best_index + 1
		digits.append(next_digit)

	joltages.append(int(''.join(map(str, digits))))


print(joltages, sum(joltages))

