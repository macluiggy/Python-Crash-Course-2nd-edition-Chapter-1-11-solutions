numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 10, 1))
print(even_numbers)

squares = []
for value in range(1,11):
     squares.append(value**2)
print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)

foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = foods[:]
foods.append('encebollado')
friend_foods.append('Chaulafan')
print("My favorite foods are:")
print(foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)