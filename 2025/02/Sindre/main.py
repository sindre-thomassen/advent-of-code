from tqdm import tqdm
import re
import time as t


VERBOSE = False
TEST = False


with open("inputs/test.txt" if TEST else "inputs/input.txt", "r") as file:
	line = file.readline()


##### Part 1 ######
def part_1(line):
	total = 0

	ranges = line.split(',')
	for _range in (tqdm(ranges) if VERBOSE else ranges):
		start, end = [int(x) for x in _range.split("-")]

		if (n_len:=len(str(start)))%2 == 1:	# Odd number, can't be invalid. Set start position to closest even length number
			start = int("1"+"0"*n_len)

		if (n_len:=len(str(end)))%2 == 1:
			end = int("9"*(n_len-1)) + 1

		for i in range(start, end+1):
			piv = str(i)
			n_len = len(piv)

			if piv[:n_len//2] == piv[n_len//2:]:
				if VERBOSE:
					print(f"Got invalid ID {i}")
		
				total += i

	return total






##### Part 1 (RegEx Solution) ######
##### Part 2 with custom RegEx pattern #####
def regex_solution(line, pattern="^(\\d+)\\1$"):
	total = 0
	
	_pattern = re.compile(pattern)
	
	ranges = line.split(',')
	for _range in (tqdm(ranges) if VERBOSE else ranges):
		start, end = [int(x) for x in _range.split("-")]

		for i in range(start, end+1):
			piv = str(i)

			if _pattern.fullmatch(piv):
				if VERBOSE:
					print(f"Got invalid ID {i}")
		
				total += i

	return total





##### Timings #####
start = t.time()
PATTERN='^(\\d+)\\1+$'
print(f"Part 1: {part_1(line)} ({t.time()-start:.2f} seconds)")
print(f"Part 1 (RegEx): {regex_solution(line)} ({t.time()-start:.2f} seconds)")
print(f"Part 2: {regex_solution(line, pattern=PATTERN)} ({t.time()-start:.2f} seconds)")