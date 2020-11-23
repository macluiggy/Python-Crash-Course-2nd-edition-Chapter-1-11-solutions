class User:
	"""Descrive several users."""
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.age = age

	def describe_user(self):
		"""Summarize and print the user's information."""
		print(f"\nFirst name: {self.first_name}")
		print(f"Last name: {self.last_name}")
		print(f"Age: {self.age}")

	def greet_user(self):
		"""Peersonalice a greeting to the user."""
		msg = f"Hello {self.first_name} {self.last_name}, you are"
		print(msg + f" {self.age} years old!")

ronaldo = User('cristiano', 'ronaldo', 37)
messi = User('lionel', 'messi', 35)
luiggy = User('luiggy', 'javier', 22)
albert = User('albert', 'einsten', 'no se compa')

ronaldo.describe_user()
ronaldo.greet_user()

messi.describe_user()
messi.greet_user()

luiggy.describe_user()
luiggy.greet_user()

albert.describe_user()
albert.greet_user()

