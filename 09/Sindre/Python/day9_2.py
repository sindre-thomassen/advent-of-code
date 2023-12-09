import numpy as np


FILE = "../input.txt"

with open(FILE) as file:
	lines = file.readlines()
	lines = [[int(x) for x in line.split(' ')] for line in lines]


def extrapolate(nums):
	next_numbers = []
	for i in range(len(nums)-1):
		next_numbers.append(nums[i+1]-nums[i])

	if (np.array(next_numbers) == 0).all():
		return nums[-1]
	else:
		return nums[-1] + extrapolate(next_numbers)


total = 0
for line in lines:
	t = extrapolate(line[::-1])
	total += t

print("Total extrapolation:", total)