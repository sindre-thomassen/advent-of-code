FILE = '../input.txt'


seed_soil_map = []
soil_firtilizer_map = []
firtilizer_water_map = []
water_light_map = []
light_temperature_map = []
temperature_humidity_map = []
humidity_location_map = []

with open(FILE) as file:
	# Seeds
	seeds = file.readline().split(' ')[1:]
	seeds = [int(seed) for seed in seeds]

	# Setup maps
	file.readline()

	for MAP in [
		seed_soil_map,
		soil_firtilizer_map,
		firtilizer_water_map,
		water_light_map,
		light_temperature_map,
		temperature_humidity_map,
		humidity_location_map
	]:
		file.readline()
		
		line = file.readline()
		while line != "\n" and line != "":
			numbers = [int(x) for x in line.split(' ')]
			MAP.append(numbers)

			line = file.readline()

MAPS = [
	seed_soil_map,
	soil_firtilizer_map,
	firtilizer_water_map,
	water_light_map,
	light_temperature_map,
	temperature_humidity_map,
	humidity_location_map
]

min_distance = float('inf')
for seed in seeds:
	current = seed
	for MAP in MAPS:
		for number_set in MAP:
			if current >= number_set[1] and current <= number_set[1] + number_set[2]:
				current = number_set[0] + (current - number_set[1])
				break
	if current < min_distance:
		min_distance = current
	
print("Shortest distance:", min_distance)