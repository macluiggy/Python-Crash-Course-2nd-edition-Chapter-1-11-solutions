def make_shirt(size= ">Shirt's size should be here<", 
	printed_message= '>the mesage goes be here<'):
	"""Display the messge that should be printed"""
	print(f"The shirt's size is {size}")
	print("This message will be printed in the" 
		f" shirt: \n {printed_message.title()}")
	print('\n')

make_shirt( printed_message= 'I love Python!')
make_shirt( size='mediun', printed_message= 'I love Python!')
make_shirt( 'small', printed_message= 'todo bien mi yabe!')