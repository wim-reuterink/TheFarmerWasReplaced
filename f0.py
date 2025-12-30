clear()

def harvest_column():
	harvest()
	for _ in range(get_world_size()-1):
		move(North)
		harvest()

def droneTask():
	move(North)
	do_a_flip()
	
while True:
	if spawn_drone(harvest_column):
		move(East)