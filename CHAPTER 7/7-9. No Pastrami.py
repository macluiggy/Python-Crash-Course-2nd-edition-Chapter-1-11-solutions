sandwich_orders = ['chicken', 'pastrami','meet', 'cheese', 'pastrami', 
'tuna', 'mortadella', 'pastrami']
finished_sandwiches = []
print("There are no pastrami sandwich anymore, we run out of it.")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print('\n')
while sandwich_orders:
	finished_sandwich = sandwich_orders.pop()
	print(f"I made your {finished_sandwich} sandwich.")
	finished_sandwiches.append(finished_sandwich)

print(f"This is the list of sandwiches you have ordered:")
for final_sandwich in finished_sandwiches:
	print(final_sandwich)