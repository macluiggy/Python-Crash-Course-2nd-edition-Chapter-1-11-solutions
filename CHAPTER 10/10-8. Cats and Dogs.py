def read(filename):
	"""Read the content of each file."""
	try:
		with open(filename) as f:
			contents = f.read()
			print(f"Reading {filename}'s contents...")
			print(contents)
			print('')
	except FileNotFoundError:
			print(f"Sorry the file {filename} does not exist.")

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
	read(filename)