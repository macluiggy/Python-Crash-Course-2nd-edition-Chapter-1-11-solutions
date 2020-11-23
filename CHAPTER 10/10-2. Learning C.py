filename = 'learning_python.txt'
message = 'In Python you can '
new_massage = message.replace('Python', 'C')

print('--Reading by looping over the file object--')
with open(filename) as f:
	for line in f:
		print(new_massage + line.strip())
		

