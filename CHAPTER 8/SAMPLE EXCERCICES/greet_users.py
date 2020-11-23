def greet_users(names):
	"""Print a simple greting to each user in the list."""
	for name in names:
		msg = f"hello, {name.title()}!"
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)