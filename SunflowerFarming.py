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
	do_a_flip()
	do_a_flip()

def plantSunflowers():
	moveTo(0,0)
	size = get_world_size()
	for i in range(size):
		for y in range(size):
			plantSingleSF()
			move(East)
		move(North)

def measureSunflowers():
	size = get_world_size()

	while True:
		readyToHarvest = True
		for i in range(size):
			for y in range(size):
				if can_harvest() == False:
					readyToHarvest = False
				move(East)
			move(North)
		if readyToHarvest:
			break
	sfMap = {}
	r = range(15, 6, -1)
	for num in r:
		sfMap[num] = []

	for i in range(size):
		for y in range(size):
			petalCount = measure()
			sfMap[petalCount].append(getLocation())
			move(East)
		move(North)
	return sfMap

def measureSunflowersV2():
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


def harvestSunflowers(sfMap):
	for pc in range(15, 6, -1):
		sfList = sfMap[pc]
		for i in range(len(sfList)):
			coordinates = sfList[i]
			#moveTo(coordinates[0], coordinates[1])
			#harvest()
			while True:
				if spawn_drone(harvestSingleFlower(coordinates[0], coordinates[1])):
					break
		do_a_flip()

def harvestSunflowersV2():
	moveTo(0,0)
	for pc in range(15, 6, -1):
		for i in range(get_world_size()):
			while True:
				if spawn_drone(harvestSpecificSizeAtColumn(pc)):
					break
			move(East)
		do_a_flip()
		do_a_flip()

def farmSunflowersV1():
	moveTo(0,0)
	plantSunflowersDrones()
	sfMap = measureSunflowers()
	harvestSunflowers(sfMap)

def farmSunflowersV2():
	moveTo(0,0)
	plantSunflowersDrones()
	sfMap = measureSunflowersV2()
	harvestSunflowers(sfMap)

def farmSunflowersV3():
	moveTo(0,0)
	plantSunflowersDrones()
	harvestSunflowersV2()

def farmSunflowers():
	farmSunflowersV3()
	
def printValues(title, powerFarmed, ticksElapsed):
	quick_print(title)
	quick_print("Power farmed:" + str(powerFarmed))
	quick_print("Ticks elapsed:" + str(ticksElapsed))

#before = num_items(Items.Power)
#beforeTC = get_tick_count()
#farmSunflowers()
#after = num_items(Items.Power)
#afterTC = get_tick_count()
#printValues("Power 1:", after - before, afterTC - beforeTC)

#before = num_items(Items.Power)
#beforeTC = get_tick_count()
#farmSunflowersv2()
#after = num_items(Items.Power)
#afterTC = get_tick_count()
#printValues("Power 2:", after - before, afterTC - beforeTC)

#before = num_items(Items.Power)
#beforeTC = get_tick_count()
#farmSunflowersv3()
#after = num_items(Items.Power)
#afterTC = get_tick_count()
#printValues("Power 3:", after - before, afterTC - beforeTC)
