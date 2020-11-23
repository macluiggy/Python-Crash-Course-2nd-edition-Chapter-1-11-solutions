numbers = list(range(1,10))
for ordinal in numbers:
	if ordinal==1:
		print(f'{ordinal}st')
	elif ordinal==2:
		print(f'{ordinal}nd')
	elif ordinal==3:
		print(f'{ordinal}rd')
	else:
		print(f'{ordinal}th')