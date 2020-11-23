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

class Admin(User):
	"""."""
	def __init__(self, first_name, last_name, age):
		"""
		Initialize the parent's class attributes.

		"""
		super().__init__(first_name, last_name,age)
		self.privileges = []

	def show_privileges(self):
		"""Show the admin's privileges."""
		print(f"\n{self.last_name} you are an admin, these are your privileges: ")
		for privilege in self.privileges:
			print('-' + privilege.title())

messi = Admin('Lionel', 'Messi', 35)
messi.privileges = [
	'can add and post',
	'can delete post',
	'can ban user'
	]

messi.describe_user()
messi.show_privileges()