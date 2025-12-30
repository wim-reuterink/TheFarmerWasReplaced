from Moving import moveTo

def plantSinglePumpkin():
	harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	use_item(Items.Water)
	plant(Entities.Pumpkin)

def plantColumnOfPumpkin():
	plantSinglePumpkin()
	for _ in range(get_world_size()-1):
		move(North)
		plantSinglePumpkin()

def initialPlant():
	for i in range(get_world_size()-2):
		while True:
			if spawn_drone(plantColumnOfPumpkin):
				move(East)
				break
	plantColumnOfPumpkin()
	move(North)
	move(East)
	plantColumnOfPumpkin()
	move(North)

def farmPumpkins():
	x, y = get_pos_x(), get_pos_y()
	for i in range(x):
		move(West)
	for i in range(y):
		move(South)
	
	firstPumpinId = 0
	lastPumpinId = 1
	
	initialPlant()
	replanted = []
	if num_items(Items.Carrot) < 1000 or num_items(Items.Wood) <1000:
		return
	for i in range(get_world_size()):
		for y in range(get_world_size()):
			if get_entity_type()!=Entities.Pumpkin:
				plantSinglePumpkin()
				replanted.append((get_pos_x(), get_pos_y()))	
			move(East)
		move(North)
	
	
	newReplanted=[]		
	while True:
		newReplanted=[]
		if len(replanted) == 0:
			break
		for i in replanted:
			moveTo(i[0], i[1])
			if get_entity_type()!=Entities.Pumpkin:
				plantSinglePumpkin()
				newReplanted.append((get_pos_x(), get_pos_y()))
		replanted = newReplanted
		
	moveTo(0,0)
	firstPumpinId = measure()
	moveTo(get_world_size()-1, get_world_size()-1)
	lastPumpinId = measure()
	if firstPumpinId == lastPumpinId:
		harvest()
		return