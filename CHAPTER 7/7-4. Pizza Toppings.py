prompt = "\nPlease enter the topping you would like to add:"
prompt += "\nEnter 'quit' to finish the order "

topping = []

while True:
	message = input(prompt)
	topping.append(message)
	if message != 'quit':
		print(message)
	else:
		print(f"You ordered the following toppings:")
		for top in topping:
			print(top)
		break
input()
