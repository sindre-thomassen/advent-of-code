import numpy as np


TEST=False


with open("./inputs/test.txt" if TEST else "./inputs/input.txt", "r") as file:
	ingredients = []
	ranges = []
	
	while (line:=file.readline().strip()):
		ranges.append(list(map(int, line.split('-'))))

	while (line:=file.readline().strip()):
		ingredients.append(int(line))

	ingredients = np.array(ingredients)



##### Part 1 #####

fresh_ingredients = set()

for start, end in ranges:
	fresh_ingredients = fresh_ingredients.union(set(ingredients[(start<=ingredients)&(ingredients<=end)]))



print(f"Part 1: {len(fresh_ingredients)}")





##### Part 2 #####


def merge_ranges(range_1, range_2):
	x1, y1 = range_1
	x2, y2 = range_2

	if (x2 <= x1 <= y2) or (x2 <= y1 <= y2) or (x1 <= x2 <= y1) or (x1 <= y2 <= y1):
		return [min(x1, x2), max(y1, y2)]

	return False


new_ranges = []

while len(ranges)>=1:
	changed = True
	next_range = ranges.pop()
	print(next_range)
	while changed:
		changed = False
		indices_to_remove = []

		for i in range(len(ranges)):

			tmp = merge_ranges(next_range, ranges[i])
			if not tmp:
				continue
			
			next_range = tmp
			ranges.pop(i)
			changed = True
			break

		

	new_ranges.append(next_range)


total = 0

for start, end in new_ranges:
	total += end - start + 1

print(total)


