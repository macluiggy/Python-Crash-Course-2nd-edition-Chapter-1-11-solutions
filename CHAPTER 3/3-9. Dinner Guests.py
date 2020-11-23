names=['Richard Feynman', 'Lana Rhoades', 'Goku']
message1='Hi'
message2='i will organize a dinner and you are invited'
fullmessage1=f'{message1.title()} {names[0].title()} {message2.title()}'
fullmessage2=f'{message1.title()} {names[1].title()} {message2.upper()}'
fullmessage3=f'{message1.title()} {names[2].title()} {message2.lower()}'
print(fullmessage1)
print(fullmessage2)
print(fullmessage3)
print(f'hi {names[0].title()} would your like some coffe?')
print(f'the numbers of guests are {len(names)}')