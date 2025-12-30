from Moving import moveToZero

def plantCactai():
	moveToZero()
	for i in range(get_world_size()):
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
	
	for i in range(get_world_size()):
		sortColumn()
		move(East)
	return

def sortHorizontally():
	moveToZero()
		
	for i in range(get_world_size()):
		sortRow()
		move(North)
	return		

def farmCactai():
	plantCactai()
	sortVertically()
	sortHorizontally()
	harvest()