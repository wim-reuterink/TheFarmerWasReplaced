from constants import getThreshold, getGraceAmount
from Planting import *
from PumpkinFarming import farmPumpkins
from CactusFarming import farmCactai
from SunflowerFarming import farmSunflowers

treeMode = True

x, y = get_pos_x(), get_pos_y()
for i in range(x):
	move(West)
for i in range(y):
	move(South)

while True:
	if num_items(Items.Wood) <= getThreshold(Items.Wood):
		treeMode = True
	if num_items(Items.Wood) >= getThreshold(Items.Wood) + getGraceAmount():
		treeMode = False

	size = get_world_size()

	if treeMode == False:
		sunflowerPlotCosts = get_cost(Entities.Sunflower)[Items.Carrot] * size * size
		if num_items(Items.Power) <= getThreshold(Items.Power) and num_items(Items.Carrot) + getGraceAmount() > sunflowerPlotCosts:
			farmSunflowers()
			continue
		
		pumpkinPlotCosts = get_cost(Entities.Pumpkin)[Items.Carrot] * size * size * 1.25
		if num_items(Items.Pumpkin) <= getThreshold(Items.Pumpkin) and num_items(Items.Carrot) + getGraceAmount() > pumpkinPlotCosts:
			farmPumpkins()
			continue	
		
		cactusPlotCosts = get_cost(Entities.Cactus)[Items.Pumpkin] * size * size
		if num_items(Items.Cactus) <= getThreshold(Items.Cactus) and num_items(Items.Pumpkin) + getGraceAmount() > cactusPlotCosts:
			farmCactai()
			continue
	
	for i in range(get_world_size()):
		for i in range(get_world_size()):
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
			move(East)
		move(North)