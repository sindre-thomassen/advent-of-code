import re

FILE = "../input.txt"

with open(FILE) as file:
	sequence = file.readline().strip()
	file.readline()
	node_map = file.readlines()


MAP = dict()


for node in node_map:
	source, left, right = re.findall("(...) = \((...), (...)\)", node)[0]
	
	MAP[source] = dict()
	MAP[source]['L'] = left
	MAP[source]['R'] = right

CURRENT = "AAA"
steps = 0
while CURRENT != "ZZZ":
	DIRECTION = sequence[steps%len(sequence)]

	steps += 1
	CURRENT = MAP[CURRENT][DIRECTION]

print(f"Reached destination in {steps} steps")