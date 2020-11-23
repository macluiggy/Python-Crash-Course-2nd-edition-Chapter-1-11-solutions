responses = {}
# set the poll to be true in the while loop

active = True
while active == True:
	# ask for the name's person and the place he wants to visit
	name = input("What is your name? ")
	place = input("What place do you want to visit the most? ")

	# Store the response in the dictionary
	responses[name] = place

	# Ask if anyone else is going to do the poll
	repeat = input("Is there anyone else whom'd like to do the poll? (yes/no) ")

	if repeat == 'no':
		active = False

# Now the poll is finished, you can print the results
print("\n--- The poll has finished ---")
print("These are the responses from the users:")

for name, place in responses:
	print(f"{name} would love to go to {place}")


print("the poll has finished. thanks for your participation")

end = input("Press 'c' to close the windows ")






