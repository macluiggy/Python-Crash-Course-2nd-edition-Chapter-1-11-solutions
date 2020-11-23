age=22
if age<2:
	person='a baby'
elif age>=2 and age<4:
	person='a toddler'
elif age>=4 and age<13:
	person= 'a kid'
elif age>=13 and age<20:
	person='a teenager'
elif age >=20 and age<65:
	person='an adult'
else:
	person='an elder'

print(f'The person is {person}')
