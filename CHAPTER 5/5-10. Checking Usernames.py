current_users=['anastacia', 'pancracio','robertototo','el brayan','superman','Deadmau5',
               'putin']
new_users=['iron man', 'deadmau5', 'micompa','sub zero','putin'] 

current_users_lower = [user.lower() for user in current_users]

for new_users in new_users:
	if new_users.lower() in current_users_lower:
		print(f'Sorry, but {new_users} has already been used, try another.')
	else:
		print(f'The username {new_users} is available')