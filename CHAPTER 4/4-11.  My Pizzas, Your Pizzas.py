pizza=['peperoni', 'queso', 'mortadela']
for pizzas in pizza:
	print(pizzas)
for pizzas in pizza:
	print(f'I like {pizzas.title()} pizza')
print('I really love pizza')

friend_pizzas=pizza[:]
pizza.append('hawaiana')
friend_pizzas.append('pollo')

print('My favorite pizzas are:')
for favorite_pizza in pizza:
	print(favorite_pizza)

print('My friend\'s favorite pizzas are:')
for favorite_friends in friend_pizzas:
	print(favorite_friends)