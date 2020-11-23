animals=['gato', 'perro', 'elefante', 'loro', 'conejo', 'ornitorrinco', 'dragon']
for pets in animals:
	print(f'A {pets} would make a grat pet.')
print('Any of these animales would make a great pet!')

print(f'The first three items in the list are: {animals[:3]}' )
print('The three items from the middle of the list are:')
for middle_animals in animals[2:5]:
	print(middle_animals.title())
print('The last three items in the list are:')
for last_three_animals in animals[-3:]:
	print(last_three_animals.title())

