prompt = "\nPlease enter the topping you would like to add:"
prompt += "\nEnter 'quit' to finish the order "

active = True

while active:
	message = input(prompt)
	if message != 'sal':
		print(message)
	else:
		active = False

	