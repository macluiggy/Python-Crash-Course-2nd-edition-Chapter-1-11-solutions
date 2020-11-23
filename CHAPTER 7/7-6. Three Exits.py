prompt = "\nPlease enter the topping you would like to add:"
prompt += "\nEnter 'quit' to finish the order "

topping = []
message= ''

while message != 'quit':
	message = input(prompt)
	topping.append(message)
	
