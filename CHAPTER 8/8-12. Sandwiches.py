def items(*sandwiches):
	"""Print the items that a sandwich will have"""
	print(f"\nMaking a sandwich with the following items:")
	for sandwich in sandwiches:
		print(f"- {sandwich}")

items('tomate', 'lechuga', 'carne de pollo')
items('queso', 'mortadela', 'salchica')
items('ese', 'man', 'ta loco')