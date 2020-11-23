import unittest
from city_functions import city_country

class PlaceTestCase(unittest.TestCase):
	"""Test for city_country.py."""

	def test_city_country(self):
		"""Do city and country such as Santiago, Chile work?."""
		formatted_place = city_country('santiago', 'chile')
		self.assertEqual(formatted_place, 'Santiago, Chile.')

if __name__ == '__main__':
	unittest.main()