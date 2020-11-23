def car_info(manufacturer, model, **options):
	"""this function show a car's information"""
	cardict = {
	'manufacturer': manufacturer.title(),
	'model': model.title(), 
	}
	for option, value in options.items():
		cardict['option'] = value

	return cardict

my_outback = car_info('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_accord = car_info('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_accord)
