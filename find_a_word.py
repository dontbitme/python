def find_a_word():
	directory = raw_input("Nazwa pliku:")
	word = raw_input("Slowo:")
	file = open(directory,"r")
	number = 0
	for valid_word in file.read().split():
		if valid_word == word:
			number += 1
		else:
			pass
	print "W pliku %s znajduje sie %r wyrazow %s." % (directory, number, word)





