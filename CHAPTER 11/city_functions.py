"""A collection of functions for working with cities."""

def city_country(city, country, population=''):
	"""Return a single string of the form City, Country."""
	if population:
		place = f"{city}, {country} - population {population}."
	else:
		place = f"{city}, {country}." 
	return place.title()