from Moving import moveToZero

def plantCactus():
	harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Cactus)

def plantColumnOfCactai():
	plantCactus()
	for _ in range(get_world_size()-1):
		move(North)
		plantCactus()

def initialPlant():
	moveToZero()
	for i in range(get_world_size()-1):
		while True:
			if spawn_drone(plantColumnOfCactai):
				move(East)
				break
	plantColumnOfCactai()
	move(North)

def plantCactai():
	moveToZero()
	for i in range(get_world_size()-1):
		for y in range(get_world_size()):
			harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)
			move(East)
		move(North)

def sortColumn():
	while True:
		swapped = False
		for y in range(get_world_size()):
			if y == get_world_size()-1:
				move(North)
				continue
				
			current = measure()
			north = measure(North)
			if current > north:
				swap(North)
				swapped = True	
			move(North)
		if swapped == False:
			return
			
def sortRow():
	while True:
		swapped = False
		for y in range(get_world_size()):
			if y == get_world_size()-1:
				move(East)
				continue
				
			current = measure()
			east = measure(East)
			if current > east:
				swap(East)
				swapped = True	
			move(East)
		if swapped == False:
			return

def sortVertically():
	moveToZero()
	
	for i in range(get_world_size()-1):
		while True:
			if spawn_drone(sortColumn):
				move(East)
				break
	sortColumn()
	move(North)
	do_a_flip()
	return

def sortHorizontally():
	moveToZero()
	
	for i in range(get_world_size()-1):
		while True:
			if spawn_drone(sortRow):
				move(North)
				break
	sortRow()
	move(North)
	do_a_flip()
	return	

def farmCactai():
	initialPlant()
	sortVertically()
	sortHorizontally()
	harvest()