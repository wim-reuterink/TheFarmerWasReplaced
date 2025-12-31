from Moving import moveTo
	
def plantMaze():
	moveTo(0,0)
	clear()
	if get_ground_type() == Grounds.Soil:
		till()
	plant(Entities.Bush)
	amoundOfWeirdSub = get_world_size() * num_unlocked(Unlocks.Mazes) * 3.2
	use_item(Items.Weird_Substance, amoundOfWeirdSub)

directions = [North, East, South, West]
def isIntersection():
	count = 0
	for direction in directions:
		if can_move(direction):
			count += 1
	return count>=3


OPPOSITE_DIRECTION = {
	North: South,
	South: North,
	East: West,
	West: East,
	None: None
}


def findTreasure(lastMove, x, y):
	startAndIntersection = False
	if lastMove == None:
		count = 0
		for direction in directions:
			if can_move(direction):
				count += 1
		if count == 2:
			startAndIntersection = True
	
	movesToRevert = []
	previousMove = lastMove
	while True:
		hasMoved = False
		if get_pos_x() == x and get_pos_y() == y:
			harvest()
			return True
	
		if isIntersection() or startAndIntersection:
			for direction in directions:
				if can_move(direction) and (direction != OPPOSITE_DIRECTION[previousMove]):
					move(direction)
					foundTreasure = findTreasure(direction, x, y)
					if foundTreasure == True:
						return True
			break
		else:
			for direction in directions:
				if can_move(direction) and direction != OPPOSITE_DIRECTION[previousMove]:
					previousMove = direction
					movesToRevert.append(direction)
					move(direction)
					hasMoved = True
					break
			if hasMoved == False:
				break
				
	for backtrackMove in movesToRevert[::-1]:
		move(OPPOSITE_DIRECTION[backtrackMove])
	if lastMove != None:
		move(OPPOSITE_DIRECTION[lastMove])
	return False


def solveMaze():
	plantMaze()
	x, y = measure()
	findTreasure(None, x, y)

while True:
	clear()	
	solveMaze()