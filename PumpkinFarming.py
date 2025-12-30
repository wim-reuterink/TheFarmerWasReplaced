from Moving import moveTo

def plantSinglePumpkin():
	if get_ground_type() != Grounds.Soil:
		till()
	harvest()
	plant(Entities.Pumpkin)

def farmPumpkins():
	x, y = get_pos_x(), get_pos_y()
	for i in range(x):
		move(West)
	for i in range(y):
		move(South)
	
	firstPumpinId = 0
	lastPumpinId = 1
	roundCount = 0
	
	replanted = []
	while True:
		newReplanted=[]
		if num_items(Items.Carrot) < 1000 or num_items(Items.Wood) <1000:
			return
		for i in range(get_world_size()):
			for y in range(get_world_size()):
				if get_entity_type()!=Entities.Pumpkin:
					plantSinglePumpkin()
					currentPosX, CurrentPosY = get_pos_x(), get_pos_y()
					newReplanted.append((currentPosX, CurrentPosY))	
				move(East)
			move(North)
		replanted = newReplanted
		roundCount = roundCount + 1
		if roundCount >= 2:
			break
			
	while True:
		newReplanted=[]
		if len(replanted) == 0:
			break
		for i in replanted:
			moveTo(i[0], i[1])
			if get_entity_type()!=Entities.Pumpkin:
				plantSinglePumpkin()
				currentPosX, CurrentPosY = get_pos_x(), get_pos_y()
				newReplanted.append((currentPosX, CurrentPosY))
		replanted = newReplanted
		
	moveTo(0,0)
	firstPumpinId = measure()
	moveTo(get_world_size()-1, get_world_size()-1)
	lastPumpinId = measure()
	if firstPumpinId == lastPumpinId:
		harvest()
		return