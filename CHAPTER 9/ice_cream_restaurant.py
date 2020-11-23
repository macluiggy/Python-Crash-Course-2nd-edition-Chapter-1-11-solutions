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