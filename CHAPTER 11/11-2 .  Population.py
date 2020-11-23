import unittest
from city_functions import city_country

class PlaceTestCase(unittest.TestCase):
	"""Test for city_country.py."""

	def test_city_country(self):
		"""Do city and country such as Santiago, Chile work?."""
		formatted_place = city_country('santiago', 'chile')
		self.assertEqual(formatted_place, 'Santiago, Chile.')

	def test_city_country_population(self):
		"""Does a place and population like 
		'Santiago, Chile – population 5000000' work?"""
		formatted_place = city_country('santiago', 'chile', population=5_000_000)
		self.assertEqual(formatted_place, f'Santiago, Chile - Population 5000000.')

if __name__ == '__main__':
	unittest.main()