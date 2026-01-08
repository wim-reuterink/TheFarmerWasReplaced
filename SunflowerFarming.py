from Moving import moveTo, getLocation

def plantSingleSF():
	harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	use_item(Items.Water)
	plant(Entities.Sunflower)


def plantColumnOfSF():
	plantSingleSF()
	for _ in range(get_world_size()-1):
		move(North)
		plantSingleSF()

def plantSunflowersDrones():
	for i in range(get_world_size()-1):
		while True:
			if spawn_drone(plantColumnOfSF):
				move(East)
				break
	plantColumnOfSF()
	move(North)
	while True:
		if num_drones() == 1:
			break

def measureSunflowers():
	sfMap = {}
	r = range(15, 6, -1)
	for num in r:
		sfMap[num] = []

	size = get_world_size()

	for i in range(size):
		for y in range(size):
			petalCount = measure()
			sfMap[petalCount].append(getLocation())
			move(East)
		move(North)
	return sfMap

def harvestSingleFlower(xcoord, ycoord):
	def	harvestSSF():
		moveTo(xcoord, ycoord)
		harvest()
	return harvestSSF

def harvestSpecificSizeAtColumn(petalCount):
	def	harvestPetalCountFromColumn():
		for i in range(get_world_size()):
			if measure() == petalCount:
				harvest()
			move(North)
	return harvestPetalCountFromColumn

def harvestSpecificSizeAtColumnWithMove(petalCount, column):
	def	harvestPetalCountFromColumnWithMove():
		moveTo(column, 0)
		for i in range(get_world_size()):
			if measure() == petalCount:
				harvest()
			move(North)
	return harvestPetalCountFromColumnWithMove


def harvestSunflowers(sfMap):
	for pc in range(15, 6, -1):
		sfList = sfMap[pc]
		for i in range(len(sfList)):
			coordinates = sfList[i]
			while True:
				if spawn_drone(harvestSingleFlower(coordinates[0], coordinates[1])):
					break
		while True:
			if num_drones() == 1:
				break

def harvestSunflowersV2():
	moveTo(0,0)
	for pc in range(15, 6, -1):
		for i in range(get_world_size()):
			while True:
				if spawn_drone(harvestSpecificSizeAtColumn(pc)):
					break
			move(East)
		while True:
			if num_drones() == 1:
				break

def harvestSunflowersV3():
	moveTo(0,0)
	for pc in range(15, 6, -1):
		for i in range(get_world_size()):
			while True:
				if spawn_drone(harvestSpecificSizeAtColumnWithMove(pc, i)):
					break
		while True:
			if num_drones() == 1:
				break

def farmSunflowersV2():
	moveTo(0,0)
	plantSunflowersDrones()
	sfMap = measureSunflowers()
	harvestSunflowers(sfMap)

def farmSunflowersV3():
	moveTo(0,0)
	plantSunflowersDrones()
	harvestSunflowersV2()

def farmSunflowersV4():
	moveTo(0,0)
	plantSunflowersDrones()
	harvestSunflowersV3()

def farmSunflowers():
	farmSunflowersV3()

def printValues(title, powerFarmed, ticksElapsed):
	quick_print(title)
	quick_print("Power farmed:" + str(powerFarmed))
	quick_print("Ticks elapsed:" + str(ticksElapsed))

# before = num_items(Items.Power)
# beforeTC = get_tick_count()
# farmSunflowersV2()
# after = num_items(Items.Power)
# afterTC = get_tick_count()
# printValues("Power 2:", after - before, afterTC - beforeTC)

before = num_items(Items.Power)
beforeTC = get_tick_count()
farmSunflowersV3()
after = num_items(Items.Power)
afterTC = get_tick_count()
printValues("Power 3:", after - before, afterTC - beforeTC)

before = num_items(Items.Power)
beforeTC = get_tick_count()
farmSunflowersV4()
after = num_items(Items.Power)
afterTC = get_tick_count()
printValues("Power 4:", after - before, afterTC - beforeTC)
