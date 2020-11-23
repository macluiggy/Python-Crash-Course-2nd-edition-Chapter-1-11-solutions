# empieze con los usuarios que necesitan ser verificados
# y una lista vacia para guardar los ususarios confirmados

usuarios_no_confirmados = ['alice', 'brian', 'candace']
usuarios_confirmados = []

# Verifique cada usuario hasta que no hayan más usuarios sin confirmar
# mueva cada usuario a la lista de usuarios confirmados

while usuarios_no_confirmados:
	usuario_actual = usuarios_no_confirmados.pop()

	print(f"Verificando usuario: {usuario_actual.title()}")
	usuarios_confirmados.append(usuario_actual)

# Muestre en pantalla todos los usuarios confirmados
print("\nLos siguientes usuarios han sido confirmados:")
for usuarios_confirmado in usuarios_confirmados:
	print(usuarios_confirmado.title())