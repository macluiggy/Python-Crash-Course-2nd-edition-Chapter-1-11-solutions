pets = []

# make each of the dictionary for each pet
pet ={
	'kind': 'loro',
	'owner': 'que andas de sapo',
}

pets.append(pet)

pet ={
	'kind': 'dog',
	'owner': 'quico',
}
pets.append(pet)

pet ={
	'kind': 'elefante',
	'owner': 'bart simpson',
}
pets.append(pet)

# now loop for each pet dictionary and print its information
for pet in pets:
	owner = pet['owner']
	kind = pet['kind']
	print(f"This is a {kind} and his owner is {owner}")