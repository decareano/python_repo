unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []


def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each design, until none are left.
	Move each design to completed_models after printing.
	"""
	i = 0
	while i < len(unprinted_designs):
		if unprinted_designs[i] == 'iphone case':
			continue
		i += 1
		current_design = unprinted_designs.pop()
		print(current_design)
				
		print(unprinted_designs)
		# Simulate creating a 3D print from the design.
		print("Printing model: " + current_design)
		completed_models.append(current_design)
		print(completed_models)
def show_completed_models(completed_models):
	"""Show all the models that were printed."""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)