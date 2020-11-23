rivers = {
	'nile': 'egypt',
	'los positos': 'sosote',
	'crucita':'crucita',
'x': 'y'	
}

for river in rivers.keys():
	if river == 'nile':
		print(f"The {river.title()} runs through {rivers[river].title()} ")
	elif river == 'los positos':
		print(f"Hable mi yabe, no quiere ir a {river.title()}?")
	elif river == 'crucita':
		print(f"{river.title()} la bella, what a beautiful place!")
	else:
		print(f"{river} is not a river and {rivers[river]} isn't a place")

print('\n')
for names in rivers.keys():
	print(names.title())

print('\n')
for place in rivers.values():
	print(place.title())