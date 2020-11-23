favorite_numbers = {
	'ron': [1, 2, 3, 4, 5],
	'angelica': [10, 20, 30, 40, 50],
	'romina': [1, 3, 5, 7, 9],
	'sonic': [2, 4, 6, 8, 10],
}

# loop through the key an value of the dictionary
for name, numbers in favorite_numbers.items():
	print(f"\n{name}'s favorite numbers are:")
	for number in numbers:
		print("- " + str(number))