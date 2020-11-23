def describe_city(city, country= 'ecuador'):
	"""Use the two parameters to display a message"""
	print(f"{city.title()} is in {country.title()}")


describe_city('crucita')
describe_city('malaga', country= 'españa')
describe_city('portoviejo')