def plantCarrots():
	if get_ground_type() == Grounds.Grassland:
		till()
	#use_item(Items.Water)
	plant(Entities.Carrot)
	#use_item(Items.Fertilizer)

def plantBush():
	if get_ground_type() == Grounds.Soil:
		till()
	#use_item(Items.Water)
	plant(Entities.Bush)

def plantPumpkin():
	if get_ground_type() != Grounds.Soil:
		till()
	#use_item(Items.Water)
	plant(Entities.Pumpkin)
	
def plantHay():
	if get_ground_type() == Grounds.Soil:
		till()

def plantTree():
	x, y = get_pos_x(), get_pos_y()
	if x % 2:
		if y % 2:
			plantHay()
			return
	else:
		if y % 2 == 0:
			plantHay()
			return
	use_item(Items.Water)
	plant(Entities.Tree)

def plantLowest():
	hayAmount = num_items(Items.Hay)
	carrotAmount = num_items(Items.Carrot)
	pumpkinAmount = num_items(Items.Pumpkin)
	if hayAmount <= carrotAmount:
		plantHay()
		return
	plantCarrots()