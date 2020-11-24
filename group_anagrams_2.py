def groupAnagrams(words):
    sortedWords = {}
	for word in words:
		sortedWord = "".join(sorted(word))
		
		if sortedWord not in sortedWords:
			sortedWords[sortedWord] = [word]
		else:
			sortedWords[sortedWord].append(word)
	
	# print(type(sortedWords))
	values = list(sortedWords.values())
	return values