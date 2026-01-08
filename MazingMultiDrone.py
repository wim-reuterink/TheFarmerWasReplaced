from Moving import moveTo
from Mazing import plantMaze

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
	count = 0
	for direction in directions:
		if can_move(direction):
			count += 1
	if count == 2:
		startAndIntersection = True
	previousMove = lastMove

	while True:
		hasMoved = False
		if get_pos_x() == x and get_pos_y() == y:
			harvest()
			return True

		if isIntersection() or startAndIntersection:
			possibleDirections = []
			for direction in directions:
				if can_move(direction) and (direction != OPPOSITE_DIRECTION[previousMove]):
					possibleDirections.append(direction)

			for i in range(len(directions)-1):
				while True:
					if spawn_drone(subDroneSolveMaze(directions.pop())):
						break
			direction = directions.pop()
			move(direction)
			previousMove = direction
		else:
			for direction in directions:
				if can_move(direction) and direction != OPPOSITE_DIRECTION[previousMove]:
					previousMove = direction
					move(direction)
					hasMoved = True
					break
			if hasMoved == False:
				break
	return False

def solveMaze():
	plantMaze()
	x, y = measure()
	findTreasure(None, x, y)

def subDroneSolveMaze(lastMove):
	def	subDroneSolveMazeParams():
		x, y = measure()
		move(lastMove)
		findTreasure(lastMove, x, y)
	return subDroneSolveMazeParams


while True:
	clear()
	solveMaze()