thresholds = {
	Items.Wood: 100100100,
	Items.Pumpkin: 27100100,
	Items.Cactus: 50100100,
	Items.Power: 100100
}
def getThreshold(item):
	return thresholds[item]

def getGraceAmount():
	return 150000