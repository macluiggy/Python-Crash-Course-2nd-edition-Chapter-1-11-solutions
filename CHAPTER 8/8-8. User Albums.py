def make_album(artist, album, trakcs=0):
	"""Show an artist's name and one of his album"""
	album = {
	'artist': artist.title(),
	 'album': album.title()
	}
	return album

	# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
		album = input(title_prompt)
		if album == 'q':
			break

		artist = input(artist_prompt)
		if artist == 'q':
			break

		album = make_album(artist, album)
		print(f"Album's information: \n{album}")



