from restaurant import Restaurant

class IceCreamStand(Restaurant):
	"""Show the type of ice cream flavors."""
	def __init__(self, name, cuisine='ice cream'):
		"""Initialize the parent class's attributes.
		Then make a attribute list of flavors.
		"""
		super().__init__(name, cuisine)
		self.flavors = []

	def show_flavors(self):
		"""Print the ice cream flavors."""
		print("List of flavors:")
		for flavor in self.flavors:
			print("-" + flavor.title())


pinguino = IceCreamStand('Pinguino')
pinguino.flavors = ['vainilla', 'chocolate', 'polito']

pinguino.describe_restaurant()
pinguino.show_flavors()


bs_cafeteria = Restaurant('BS Cafeteria', 'Breakfast')

print(bs_cafeteria.name)
print(bs_cafeteria.cuisine)