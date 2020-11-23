movies=['fight club', 'el padrino', 'la sirenita']
sorted(movies)
print("alphabetical temporarly")
print(sorted(movies))

print("\n original order")
print(movies)

print('\n Reverse alphabetical sorted order')
print(sorted(movies, reverse=True))

print('\n Original reverse order')
movies.reverse()
print(movies)

print('\n Reverse original reverse order')
movies.reverse()
print(movies)

print('\n Alphabetical permanent order')
movies.sort()
print(movies)

print('\n Reverse Alphabetical permanent order')
movies.sort(reverse=True)
print(movies)
movie1='fight club'
movies.remove(movie1)
print(f"It seem that {movie1.title()} have been removed from the cartelera")
print(movies)
