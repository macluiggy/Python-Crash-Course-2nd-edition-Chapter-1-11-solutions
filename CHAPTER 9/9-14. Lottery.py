from random import choice

possibilities = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []

# We don't want to repeat winning numbers or letters, so we'll use a 
# While loop

while len(winning_ticket) < 4:
	pulled_item = choice(possibilities)

	# Only add the pulled item to the winning ticket if it hasn't
	# already been pulled.
	if pulled_item not in winning_ticket:
		print(f"We pulled a {pulled_item}!")
		winning_ticket.append(pulled_item)

print(f"The final winning ticket is: {winning_ticket}")