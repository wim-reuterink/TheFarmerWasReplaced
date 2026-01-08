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
	for i in range(get_world_size()-1):
		while True:
			if spawn_drone(plantColumnOfPumpkin):
				move(East)
				break
	plantColumnOfPumpkin()
	move(North)


def replantColumnFullCheck():
	replanted = False
	for y in range(get_world_size()):
		if get_entity_type() != Entities.Pumpkin:
			plantSinglePumpkin()
			replanted = True
		move(North)
	if replanted == False:
		return
	do_a_flip()
	replantColumn()

def replantColumn():
	replanted = []
	for y in range(get_world_size()):
		if get_entity_type() != Entities.Pumpkin:
			plantSinglePumpkin()
			replanted.append((get_pos_x(), get_pos_y()))
		if can_harvest() == False:
			replanted.append((get_pos_x(), get_pos_y()))
		move(North)
	newReplanted=[]
	while True:
		newReplanted=[]
		if len(replanted) == 0:
			break
		for i in replanted:
			moveTo(i[0], i[1])
			if get_entity_type() != Entities.Pumpkin:
				plantSinglePumpkin()
				newReplanted.append((get_pos_x(), get_pos_y()))
		replanted = newReplanted
	replantColumnFullCheck()

def measureUntilHarvest():
	moveTo(0,0)
	while True:
		if num_drones() == 1:
			break
	harvest()

def farmPumpkinsWithDrones():
	moveTo(0,0)
	initialPlant()

	for i in range(get_world_size()):
		while True:
			if spawn_drone(replantColumn):
				move(East)
				break

	measureUntilHarvest()

#farmPumpkinsWithDrones()