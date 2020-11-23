import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Test for the module employee."""

	def setUp(self):
		"""Make an employee to use in the test."""
		self.luiggy = Employee('luiggy', 'macias', 65_000)

	def test_give_default_raise(self):
		"""Test the default amount of salary."""
		self.luiggy.give_raise()
		self.assertEqual(self.luiggy.salary, 70000)

	def test_give_custom_raise(self):
		"""Test the custom amount of the salary."""
		self.luiggy.give_raise(10000)
		self.assertEqual(self.luiggy.salary, 75000)

if __name__ == '__main__':
	unittest.main()
