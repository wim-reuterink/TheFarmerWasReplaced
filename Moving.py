def moveToZero():
	x, y = get_pos_x(), get_pos_y()
	for i in range(x):
		move(West)
	for i in range(y):
		move(South)
		
def moveTo(x, y):
	currentX, currentY = get_pos_x(), get_pos_y()
	deltaX = x - currentX
	deltaY = y - currentY
	if deltaX < 0: 
		for i in range(deltaX*-1):
			move(West)
	else:
		for i in range(deltaX):
			move(East)
	if deltaY < 0: 
		for i in range(deltaY*-1):
			move(South)
	else:
		for i in range(deltaY):
			move(North)

def getLocation():
	return (get_pos_x(), get_pos_y())