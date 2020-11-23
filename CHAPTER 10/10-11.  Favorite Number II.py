import json

filename = 'favorite_number.json'
with open (filename) as f:
	favnumber = json.load(f)

print(f"I know your favorite number! It's {favnumber}")