import re


FILE = "../input.txt"

with open(FILE) as file:
	time = int(''.join([x for x in re.findall("[0-9]+", file.readline())]))
	dist = int(''.join([x for x in re.findall("[0-9]+", file.readline())]))


def calc_wins(max_time, to_beat):
	wins = 0
	for i in range(1, max_time):
		distance = i*(max_time-i)

		if distance > to_beat:
			wins += 1

	return wins

wins = calc_wins(time, dist)

print("Total ways of winning:", wins)