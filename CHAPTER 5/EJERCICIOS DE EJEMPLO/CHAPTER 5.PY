cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
     if car == 'bmw':
        print(car.upper())
     else:
        print(car.title())

 #toppings.py
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("\nHold the anchovies!")

#MAGIC_NUMBER.py
answer = 17
if answer != 42:
    print("\nThat is not the correct answer. Please try again!")

 #banned  _users.py 
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"\n{user.title()}, you can post a response if you wish.")

#amusement_park.py
age=12
print('\n')
if age<4:
	print('Your admission cost $0.')
elif age<18:
	print('Your admission cost $25.')
else:
	print("Your admission cost $40.")

age=12
print('\n')
if age<4:
	price=0
elif age<18:
	price=25
else:
	price=40
print(f'Your admission cost is ${price}.')

print('\n')
age=120
print('\n')
if age<4:
	price=0
elif age<18:
	price=25
elif age< 65:
	price=40
else:
	price=20
print(f'Your admission cost is ${price}.')

print('\n')
age=120
print('\n')
if age<4:
	price=0
elif age<18:
	price=25
elif age< 65:
	price=40
elif age>=65:
	price=20
print(f'Your admission cost is ${price}.')

#toppings.py
requested_topping=['mushrooms', 'extra cheese']
if 'mushrooms' in requested_topping:
	print('Adding mushrooms.')
if 'pepperoni' in requested_topping:
	print('Adding pepperoni.')
if 'extra cheese' in requested_topping:
	print('Adding extra cheese.')

print('\nFinished making your pizza!')

#toppings.py
print('\n')
requested_topping=['mushrooms','green peppers', 'extra cheese']
for requested_topping in requested_topping:
	if requested_topping=='green peppers':
		print('Sorry, we are out of green peppers right now. Ohhh the shuro')
	else:
		print(f'Adding {requested_topping} ')
print('Finished making your pizza!')

print('\n')
requested_topping=[]
if requested_topping:
	for requested_topping in requested_topping:
		print(f'Adding {requested_topping}.')
	print('Finished making your pizza!')
else:
	print('Are you sure you want a plain pizza?')

print('\n')
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_topping= ['mushrooms','olives', 'green peppers','guatita']
for requested_topping in requested_topping:
	if requested_topping in available_toppings:
		print(f'Adding {requested_topping}')
	else:
		print(f'Sorry, we dont\'n have {requested_topping}')

print('\nFinished making your pizza')
