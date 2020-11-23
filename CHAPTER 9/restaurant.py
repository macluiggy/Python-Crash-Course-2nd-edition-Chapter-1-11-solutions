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