def show_message(messages):
    """Print the name of each magician in the list."""
    while messages:
    	current_message = messages.pop()
    	print(f"The message '{current_message}'' is being moved to"
    		" send_messages_list")
    	send_messages_list.append(current_message)

def send_messages(send_messages_list):
	"""Show the messaged that were moved."""
	print(f"This messages have been moved to send_messages_list: ")
	for send_message_list in send_messages_list:
		print(send_message_list)


messages = ['harry houdini', 'david blaine', 'teller']
send_messages_list = []

show_message(messages)
send_messages(send_messages_list)

