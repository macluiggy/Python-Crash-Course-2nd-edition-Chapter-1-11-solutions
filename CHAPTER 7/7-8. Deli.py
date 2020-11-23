sandwich_orders = ['chicken', 'meet', 'cheese', 'tuna', 'mortadella']
finished_sandwiches = []

while sandwich_orders:
	finished_sandwich = sandwich_orders.pop()
	print(f"I made your {finished_sandwich} sandwich.")
	
	finished_sandwiches.append(finished_sandwich)

print(f"This is the list of sandwiches you have ordered:")
for final_sandwich in finished_sandwiches:
	print(final_sandwich)