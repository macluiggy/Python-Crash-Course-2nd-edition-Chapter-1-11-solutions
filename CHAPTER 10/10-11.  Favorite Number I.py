import json

filename = 'favorite_number.json'
favnumber = input("What is your favorite number? ")
favnumber = int(favnumber)
with open (filename, 'w') as f:
	json.dump(favnumber, f)
	print(f"Your favorite number {favnumber} now it's stored!")

input()