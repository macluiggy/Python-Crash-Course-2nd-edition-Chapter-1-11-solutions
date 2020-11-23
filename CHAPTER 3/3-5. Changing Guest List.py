names=['Richard Feynman', 'Lana Rhoades', 'Goku']
print(names)
message1='Hi'
message2='i will organize a dinner and you are invited'
fullmessage1=f'{message1.title()} {names[0].title()} {message2.title()}'
fullmessage3=f'{message1.title()} {names[2].title()} {message2.lower()}'
lana='Lana Rhoades'
print(fullmessage1)
print(fullmessage3)
print(f"It seems {lana.title()} can't attend the invitation")
names[1]='Doraemon'
print(f'Hi {names[1].title()} you are invited to my super incredible dinner, if you want, bring Nobita with you')
print(names)
