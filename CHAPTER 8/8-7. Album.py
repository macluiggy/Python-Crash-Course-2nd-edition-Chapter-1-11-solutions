def make_album(artist, album, nsongs=0):
	"""Show an artist's name and one of his album"""
	album = {'artist': artist.title(), 'album': album.title()}
	if nsongs:
		album['Number of songs'] = f"{nsongs.title()} songs"
	return album


album= make_album('the beatles', 'revolver', '13')
print(album)

artist_album= make_album('deadmau5', '>album title goes here<', '11')
print(artist_album)

artist_album= make_album('luis fonsi', 'despacito')
print(artist_album)