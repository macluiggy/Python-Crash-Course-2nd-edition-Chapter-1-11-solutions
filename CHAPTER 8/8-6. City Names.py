def city_country(city, country):
	"""Display a message of a city and its country."""
	unido = f"{city}, {country}"
	return unido

location = city_country('c', 's')
print(location.title())

location = city_country('cricita', 'ecuador')
print(location.title())

location = city_country('portoviejo', 'manabi')
print(location.title())