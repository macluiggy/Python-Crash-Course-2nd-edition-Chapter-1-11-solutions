my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for my_foods in my_foods:
	print(my_foods.title())

print("\nMy friend's favorite foods are:")
for friend_foods in friend_foods:
    print(friend_foods.title())