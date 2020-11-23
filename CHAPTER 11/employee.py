class Employee:
	"""A class to represent an employee."""

	def __init__(self, first, last, salary):
		"""Initialize the employee."""
		self.first = first
		self.last = last
		self.salary = salary

	def give_raise(self, amount=5000):
		"""Give a raise to the employee."""
		self.salary += amount