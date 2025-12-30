from Moving import moveTo, getLocation

def plantSingleSF():
	harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Sunflower)

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

def harvestSunflowers(sfMap):
	for pc in range(15, 6, -1):
		sfList = sfMap[pc]
		for i in range(len(sfList)):
			coordinates = sfList[i]
			moveTo(coordinates[0], coordinates[1])
			harvest()

def farmSunflowers():
	plantSunflowers()
	sfMap = measureSunflowers()
	harvestSunflowers(sfMap)