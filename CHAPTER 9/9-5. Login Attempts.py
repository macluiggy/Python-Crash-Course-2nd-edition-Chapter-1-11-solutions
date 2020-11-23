class User:
	"""Descrive several users."""
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.age = age
		self.login_attempts = 0

	def describe_user(self):
		"""Summarize and print the user's information."""
		print(f"\nFirst name: {self.first_name}")
		print(f"Last name: {self.last_name}")
		print(f"Age: {self.age}")

	def greet_user(self):
		"""Peersonalice a greeting to the user."""
		msg = f"Hello {self.first_name} {self.last_name}, you are"
		print(msg + f" {self.age} years old!")

	def increment_login_attempts(self):
		"""Increment the value of login_ttempts by 1."""
		self.login_attempts += 1
		print(f"Number of login attempts: {self.login_attempts}")

	def reset_login_attempts(self):
		"""Reset the value of login_attempts to 0."""
		self.login_attempts = 0
		print(f"Number of login attempts: {self.login_attempts}")


ronaldo = User('cristiano', 'ronaldo', 37)

ronaldo.describe_user()
ronaldo.greet_user()

ronaldo.increment_login_attempts()
ronaldo.increment_login_attempts()
ronaldo.increment_login_attempts()
ronaldo.increment_login_attempts()

ronaldo.reset_login_attempts()
ronaldo.increment_login_attempts()