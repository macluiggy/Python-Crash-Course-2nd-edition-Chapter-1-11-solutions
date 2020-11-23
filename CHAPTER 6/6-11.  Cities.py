cities = {
	'portoviejo': {
	'country': 'ecuador',
	'population':'16 000 000',
	'fact': 'its the Manabís capital',
	},
	'new york': {
	'country': 'Unites States',
	'population': '10e6',
	'fact': 'worlds capital',
	},
	'crucita': {
	'country': 'ecuador',
	'population': 'no se mi yabe',
	'fact': 'uno se puede bañar en sus playas',
	}
}

for city, information_city in cities.items():
	print(f"\n{city} city's information:")
	for key, value in information_city.items():
		print(f"\t{key}:")
		print("\t\t" + str(value))
