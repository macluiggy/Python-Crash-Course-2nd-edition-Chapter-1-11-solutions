from user import User

class Admin(User):
	"""."""
	def __init__(self, first_name, last_name, age):
		"""
		Initialize the admin.
		"""
		super().__init__(first_name, last_name,age)

		# Initialize an empty set of privileges.
		self.privileges = Privileges([])


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
luiggy_privileges = [
	'Can erase comments',
	'can ban a user',
	'can eliminate a publish'
]
luiggy.privileges.privileges = luiggy_privileges
luiggy.privileges.show_privileges()