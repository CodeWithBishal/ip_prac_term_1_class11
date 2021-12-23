input_sentence = input("Please enter a sentence: ")
words = input_sentence.split()
dictionary = {}
for word in words:
	if (word[0] not in dictionary.keys()):
		dictionary[word[0]] = []
		dictionary[word[0]].append(word)
		print(dictionary)
	else:
		if (word not in dictionary[word[0]]):
			dictionary[word[0]].append(word)
