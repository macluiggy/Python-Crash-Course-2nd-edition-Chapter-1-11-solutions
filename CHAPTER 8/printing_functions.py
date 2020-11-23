def print_models(unprinted_designs, complete_models):
	"""
	simulate printing each design until none are left.
	Move each design to complete_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		complete_models.append(current_design)

def show_completed_models(complete_models):
	"""Show all the models that were printed."""
	print("\nThe following models have been printed:")
	for complete_model in complete_models:
		print(complete_model)