import json

def get_stored_user():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Prompt for a new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

def greet_user():
	"""Greet the user by name."""
	username = get_stored_user()
	response = input(f"Are your {username}? (y/n): ")
	if response == 'y':
		if username:
			msg = f"Welcome back {username}!"
			print(msg.title())
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}")

greet_user()
input()