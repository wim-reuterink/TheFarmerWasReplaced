from constants import getThreshold, getGraceAmount
from Planting import *
from PumpkinFarming import farmPumpkins, farmPumpkinsWithDrones
from CactusFarming import farmCactai
from SunflowerFarming import farmSunflowers
from Moving import moveTo, moveToZero, getLocation

treeMode = True

moveToZero()
def regularFarmingSingle():
	if get_entity_type() == Entities.Dead_Pumpkin:
		plantLowest()
	if can_harvest():	
		harvest()
		if treeMode:
			plantTree()
		else:
			plantLowest()
	if get_entity_type() == None:
		if treeMode:
				plantTree()
		else:
			plantLowest()

def regularFarmingOfColumn():
	for i in range(get_world_size()-1):
		regularFarmingSingle()
		move(North)
	regularFarmingSingle()

while True:
	moveToZero()
	if num_items(Items.Wood) <= getThreshold(Items.Wood):
		treeMode = True
	if num_items(Items.Wood) >= getThreshold(Items.Wood) + getGraceAmount():
		treeMode = False

	size = get_world_size()
	sunflowerPlotCosts = get_cost(Entities.Sunflower)[Items.Carrot] * size * size
	if num_items(Items.Power) <= getThreshold(Items.Power) and num_items(Items.Carrot) + getGraceAmount() > sunflowerPlotCosts and num_items(Items.Water) + getGraceAmount() > size*size:
		treeMode = False
		farmSunflowers()
		continue

	if treeMode == False:
		pumpkinPlotCosts = get_cost(Entities.Pumpkin)[Items.Carrot] * size * size * 1.25
		if num_items(Items.Pumpkin) <= getThreshold(Items.Pumpkin) and num_items(Items.Carrot) + getGraceAmount() > pumpkinPlotCosts and num_items(Items.Water) + getGraceAmount() > size*size:
			farmPumpkinsWithDrones()
			continue	
		
		cactusPlotCosts = get_cost(Entities.Cactus)[Items.Pumpkin] * size * size
		if num_items(Items.Cactus) <= getThreshold(Items.Cactus) and num_items(Items.Pumpkin) + getGraceAmount() > cactusPlotCosts:
			farmCactai()
			continue
	
	for i in range(get_world_size()):
		while True:
			if spawn_drone(regularFarmingOfColumn):
				break
		move(East)
		