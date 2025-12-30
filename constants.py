thresholds = {
	Items.Wood: 9100100,
	Items.Pumpkin: 2100100,
	Items.Cactus: 1100100,
	Items.Power: 1100
}
def getThreshold(item):
	return thresholds[item]

def getGraceAmount():
	return 150000