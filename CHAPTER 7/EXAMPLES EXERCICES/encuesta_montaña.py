respuestas = {}

# Estableszca una bandera para indicar ue la encuesta esta activa
encuesta_activa = True

while encuesta_activa :
	# solicite el nombre y la respuesta de la persona encuestada
	nombre = input("\nCual es tu nombre? ")
	respuesta = input("Que montaña te gustaria escalar alguna vez?")

	# Guarde la respuesta en el diccionario.
	respuestas[nombre] = respuesta

	# Pregunte si alguien mas va a hacer la encuesta.
	repetir = input("Te gustaria dejar que otra persona responda la encuesta? (si/no) ")
	if repetir == 'no':
		encuesta_activa = False

# La encuesta esta completa. Muestre los resultados,
print("\n--- Resultados de la encuesta ---")
for nombre, respuesta in respuestas.items():
	print(f"A {nombre} le gustaria escalar la montaña {respuesta}.")

input()