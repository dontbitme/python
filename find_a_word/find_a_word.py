def find_a_word():
	directory = raw_input("Nazwa pliku:")
	word = raw_input("Slowo:")
	countWords(directory, word)
	print "W pliku %s znajduje sie %r wyrazow %s." % (directory, number, word)

def countWords(filename, word):
	file = open(filename,"r")
	number = 0
	for valid_word in file.read().split():
		if valid_word == word:
			number += 1
	return number





