def add_items(new_items, base_items=None):
	 if base_items is None:
	         base_items = []
	 for item in new_items:
	     base_items.append(item)
	 return base_items

print(add_items((1,2,3)))

print(add_items((2,3,4)))
