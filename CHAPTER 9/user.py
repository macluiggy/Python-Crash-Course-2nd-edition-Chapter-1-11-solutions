class User:
	"""Descrive several users."""
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.age = age

	def describe_user(self):
		"""Summarize and print the user's information."""
		print(f"First name: {self.first_name}")
		print(f"Last name: {self.last_name}")
		print(f"Age: {self.age}")

	def greet_user(self):
		"""Peersonalice a greeting to the user."""
		msg = f"Hello {self.first_name} {self.last_name}, you are"
		print(msg + f" {self.age} years old!")

