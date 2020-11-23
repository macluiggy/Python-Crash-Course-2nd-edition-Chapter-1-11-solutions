prompt = "\nPor favor ingrese el nombre de una ciudad que haya visitado:"
prompt += "\n(Ingrese 'quit' cuando haya acabado)"

while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print(f"Me gustaria ir a la ciudad {city.title()}")