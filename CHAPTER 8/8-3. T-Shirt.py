def make_shirt(size, printed_message= '>the mesage goes be here<'):
	"""Display the messge that should be printed"""
	print(f"The shirt's size is {size}")
	print("This message will be printed in the" 
		f" shirt: \n {printed_message.title()}")

make_shirt('22', printed_message= 'just do it!')