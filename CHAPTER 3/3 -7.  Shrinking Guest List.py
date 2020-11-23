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
print('Wow, it seem there is more space available for the table, i will invite some more guests')
names.insert(0, 'Mi compa')
names.insert(2, 'John Cena')
names.append('batman')
print(fullmessage1)
print(fullmessage3)
print(f'Hi {names[0].title()} your are a new guest of my expectacular dinnder :)')
print(f'Hi {names[2].title()} your are a new guest of my expectacular dinnder :)')
print(f'Hi {names[5].title()} your are a new guest of my expectacular dinnder :)')
print('BREAKING NEWS! Sorry but it seems there aret enough cocacola for everyones, so there are just room just for two')
uninvited1=names.pop(0)
print(f'Sorry {uninvited1.title()} but the plans have changed, you are no invited now')
uninvited2=names.pop(1)
print(f'Sorry {uninvited2.title()} but the plans have changed, you are no invited now')
uninvited3=names.pop(0)
print(f'Sorry {uninvited3.title()} but the plans have changed, you are no invited now')
uninvited4=names.pop(0)
print(f'Sorry {uninvited4.title()} but the plans have changed, you are no invited now')
print(f"Don't worry {names[0].title()} you are still invited")
print(f"Don't worry {names[1].title()} you are still invited")
print(names)
del names[0]
del names[0]
print(names)