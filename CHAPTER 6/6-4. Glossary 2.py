programming_words={
'loop':'work in a list of words, one at a time',
'list':'a collection of word stored in a list which you can use as a single'
' variable',
'if-elif-else':'a set of condition to do a determinate accion when one of the'
' conditions is true',
'dictionery':'a collection of key-value pairs.',
'comment': 'a comentary that help you to understand more complex code',
'perro': 'an animal that says wau wau',
'gato': 'the same thing but instead of "wau wau" is "miau"',
'variable': 'a word that store information',
'print()':'This is useful when you want to display a message',
}

for word in programming_words.keys():
	meaning = programming_words[word]
	print(f"\n{word}: {meaning} ")