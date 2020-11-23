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
		Initialize the admin.
		"""
		super().__init__(first_name, last_name,age)

		# Initialize an empty set of privileges.
		self.privileges = Privileges()


class Privileges():
	"""."""

	def __init__(self, privileges=[]):
		self.privileges = privileges
	

	def show_privileges(self):
		print("\nPrivileges:")
		if self.privileges:
			for privilege in self.privileges:
				print('-' + privilege)
			else:
				print('- This user has no privileges.')


luiggy = Admin('luiggy', 'macias', 22)
luiggy.describe_user()

luiggy.privileges.show_privileges()

print("\nAdding privileges...")
luiggy_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
luiggy.privileges.privileges = luiggy_privileges
luiggy.privileges.show_privileges()

