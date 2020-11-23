#1
letters=['a', 'b', 'c', 'd', 'e']
print(letters[0]=='a')
print(letters[-1]=='E')
print('\n')
#2
perro='Firulais'
perro.lower=='firulais'
print(perro.lower()=='firulais')
print(perro.lower()=='Firulais')
print('\n')
#3
n1=10; n2=20
print(n1+n2==30)
print(n1-30==-n2)
print(n1+n2!=30)
print(n1-30!=-n2)

print('\n')
print(n1+1>n1)
print(n1>n1+1)
print(n1-n2<=0)
print(n1*n1<=n1**2-1)

#5
print((n1+n2)**2==n1**2+2*n1*n2+n2**2 and n1==10)
print(n2-n1==n1 or n2=='perro')
animals=['perro', 'gato', 'loro']
print(animals[0]=='perro' and animals[1]=='carro')
print(animals[0]=='perro' or animals[1]=='carro')

#6
print(animals[0]=='john cena')
print(animals[2]=='loro')
print('john cena' in animals)
print('loro' in animals)
print('john cena' not in animals)
print('loro' not in animals)