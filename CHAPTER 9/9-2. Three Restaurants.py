class Restaurant:
	"""docstring for ClassName"""
	def __init__(self, name, cuisine):
		"""fgfg"""
		self.name = name
		self.cuisine = cuisine

	def describe_restaurant(self):
		"""Describe the restaurant."""
		print(f"The {self.name} restaurant has the best {self.cuisine}")

	def open_restaurant(self):
		"""Indicate that the restaurant is open."""
		print(f"{self.name} restaurant is now open")

bs_cafeteria = Restaurant('BS Cafeteria', 'Breakfast')
encebollado_laturra = Restaurant('La turra', 'Encebollado')
helados_pepito = Restaurant('Helados Pepito', 'helados')

bs_cafeteria.describe_restaurant()
encebollado_laturra.describe_restaurant()
helados_pepito.describe_restaurant()