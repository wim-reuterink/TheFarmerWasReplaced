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
	while True:
		readyToHarvest = True
		size = get_world_size() 
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
	
def harvestSingleFlower(xcoord, ycoord):
	def	harvestSSF():
		moveTo(xcoord, ycoord)
		harvest()
	return harvestSSF	

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

def farmSunflowers():
	moveTo(0,0)
	plantSunflowersDrones()
	sfMap = measureSunflowers()
	harvestSunflowers(sfMap)
	
#farmSunflowers()