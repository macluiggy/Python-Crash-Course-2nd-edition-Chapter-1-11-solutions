# Write a program that prompts for two numbers. Add them
# togheter and print the result.
print("Give me two numbers and I'll add them")
print("Press 'q' to quit")

while True:
	num1 = input("First number: ")
	num2 = input("Second number: ")
	if num1 == 'q':
		break
	if num2 == 'q':
		break
	try:
		result = int(num1) + int(num2)
	except ValueError:
		print("Just can accept numbers")
	else:
		print(f"The result is {result}")