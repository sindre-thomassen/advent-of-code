import re


FILE = "../input.txt"

with open(FILE) as file:
	times = [int(x) for x in re.findall("[0-9]+", file.readline())]
	distances = [int(x) for x in re.findall("[0-9]+", file.readline())]

races = zip(times, distances)



def calc_wins(max_time, to_beat):
	wins = 0
	for i in range(1, max_time):
		distance = i*(max_time-i)

		if distance > to_beat:
			wins += 1

	return wins

total = 1
for time, dist in races:
	wins = calc_wins(time, dist)
	total *= wins

print("Total ways of winning:", total)