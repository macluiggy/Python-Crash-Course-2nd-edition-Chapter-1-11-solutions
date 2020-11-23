favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

print('\n')
names = ['compa', 'david', 'jen', 'phil']
print(names)

for name in names:
	if name in favorite_languages:
		print(f"Thank you {name} for responding our poll.")
	else:
		print(f"Hi {name}, would you like to take the poll?")