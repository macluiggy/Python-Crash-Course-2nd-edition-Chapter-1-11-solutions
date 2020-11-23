prompt = "How old are you?"
prompt += "\nEnter 'exit' to finish "

cost = 0

message = ''
while message != 'quit':
	age = input(prompt)
	age = int(age)
	if age < 3:
		print(f"Your ticket is free becouse you are {age} years old")
	elif age < 12:
		print(f"Your ticket costs $10, because you are {age} years old")
	else:
		print(f"Your ticket costs $15, because you are {age} old")

