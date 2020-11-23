gato='misirrongo'
print('The name of your cat is pelusa:')
print(gato=='pelusa')

print('\nThe name of your cat is misirrongo:')
print(gato=='misirrongo')

#TRUE BOOLEANS
#1
colors=['red', 'yellow', 'white',]
my_cars=['bmw', 'lamorgini']

print('Car is not a color, am i right?')
print('Yes you are right that is:')
print(colors!='bmw')

#2
january=31
march=31
print(january==31 and march ==31)

#3
print('I have a lamorgini:')
print('lamorgini' in my_cars)

#4
movies=['Sherk','Sherk 2', 'Sherk 3', 'Sherk 4', 'Sherk 5']
print('This is the Sherk\'s saga movies that are in the cartelera:')
print(movies)
print('Oh, it seems Sherk 5 is going to be removed from the cartelera becouse') 
print('the movie will be cancelled')
movies.pop(4)
print('-Have Sherk 5 been removed from the cartelera?')
print('Sherk 5' not in movies)
print('Now this is the new cartelera:')
print(movies)

num1=0
num2=0
print('Are number 1 and number 2 the same value:')
print(num1==num2)
#FALSE BOOLEANS
#1
February=28
July=31
print('February and July have more than 30 days:')
print(February>30 and July>30)

#2
items=['item 1', 'item 2', 'item 3','item 4']
print('I need the item 3 no longer, so remove it from the list')
print('The item 3 will be removed at 6 pm')
current_hour=7
print('The item 3 have been removed before the settled hour:')
print(items[2]!='item 3')
if current_hour >= 6:
	items.pop(2)
	print('The item 3 is still in the list:')
	print(items[2]=='item 3')

#3
num=10
print(num>11)

#4
print(num/10!=1)

#5
print(num+num<=19)

