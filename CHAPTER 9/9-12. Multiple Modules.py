from admin import Admin

luiggy = Admin('luiggy', 'macias', 22)
luiggy_privileges = [
	'Can erase comments',
	'can ban a user',
	'can eliminate a publish'
]
luiggy.privileges.privileges = luiggy_privileges
luiggy.privileges.show_privileges()