import re
import numpy as np


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


CURRENT = [node for node in MAP.keys() if node[-1]=="A"]
# CURRENT = np.array([list("AAA"), list("FSA")])
# CURRENT = ["AAA", "FSA"]

steps = 0


# def check_winning_condition(nodes):
# 	return (nodes[:, -1] == 'Z').all()

def check_winning_condition(nodes):
	return all(map(lambda x: x[-1] == 'Z', nodes))


FOUND = False
while not FOUND:
	DIRECTION = sequence[steps%len(sequence)]
	steps += 1

	# CURRENT = np.array([list(MAP[''.join(node)][DIRECTION]) for node in CURRENT])
	CURRENT = [MAP[node][DIRECTION] for node in CURRENT]
	if CURRENT[0][-1] == "Z":
		FOUND = check_winning_condition(CURRENT)

print(f"Reached destination in {steps} steps")