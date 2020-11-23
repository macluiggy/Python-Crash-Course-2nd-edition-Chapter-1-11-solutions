class Restaurant:
	"""docstring for ClassName"""
	def __init__(self, name, cuisine):
		"""fgfg"""
		self.name = name
		self.cuisine = cuisine
		self.number_served = 0

	def describe_restaurant(self):
		"""Describe the restaurant."""
		print(f"The {self.name} restaurant has the best {self.cuisine}")

	def open_restaurant(self):
		"""Indicate that the restaurant is open."""
		print(f"{self.name} restaurant is now open")

	def customers_served(self):
		"""Show how many customers have been served."""
		print(f"The restaurant have sereved to {self.number_served} customers!")

	def update_customers_served(self, updated_number):
		self.number_served = updated_number

	def increment_number_served(self, incremented_number):
		"""Increment the number of customers that have been served."""
		self.number_served += incremented_number


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
