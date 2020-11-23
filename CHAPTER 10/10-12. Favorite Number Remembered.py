import json

filename = 'favorite_numer.json'
try:
	with open(filename) as f:
		favnumber = json.load(f)
		print(f"Your favorite number is {favnumber}!")
except FileNotFoundError:
	favnumber = input("What is your favorite number? ")
	with open(filename, 'w') as f:
		json.dump(favnumber, f)
		print(f"Your favorite number {favnumber} has been stored!")

input()