# Choice a file and show how many times a specific word appears
# in the file.
filename = 'potions.txt'

try:
	with open(filename, encoding='utf-8') as f:
		contents = f.read()
except UnicodeDecodeError:
	pass
except FileNotFoundError:
    print(f"Sorry, I couldn't find that file")
else:
	word_count = contents.lower().count('the')
	print(f"The file {filename} has about {word_count} the word 'the'")