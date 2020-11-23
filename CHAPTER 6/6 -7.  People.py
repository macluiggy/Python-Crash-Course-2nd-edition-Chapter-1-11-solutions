batman = {
'first name': 'bruce',
'last name': 'wayne', 
'age': 40, 
 'city': 'gotam'
}
people1 = {
	'age': 10,
	'height': 1.50,
	'favorite meal': 'hamburger',
	'ocupation': 'student,'
}

people2 = {
	'age': 22,
	'height': 1.75,
	'favorite meal': 'encebollado',
	'ocupation': 'superhero',
}

people3 = {
	'age': 1000,
	'height': 1.8,
	'favorite meal': 'empanada',
	'ocupation': 'ghost',
}
print(batman['first name'])
print(batman['last name'])
print(batman['age'])
print(batman['city'])

people = [people1, people2, people3]
for person in people:
	for general, particular in person.items():
		print(f"\n{general}: {particular}")