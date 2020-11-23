filename = 'learning_python.txt'

print('--Reading in the entire file--')
with open(filename) as file_object:
	contents = file_object.read()
	print(contents)

print('\n--Reading by looping over the file object--')
with open(filename) as f:
	for line in f:
		print(f"In Python you can {line.strip()}")

print('\n--Reading by storing the lines in a list and the working'
	' with them outside the with block--y')
with open(filename) as f:
	lines = f.readlines()

for line in lines:
	print(f"In Python you can {line.rstrip()}")






