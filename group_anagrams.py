def groupAnagrams(words):
    # Write your code here.
	result = []
    for i in range(0, len(words)):
		letterCount = {}
		sub = [words[i]]
		
		for letter in words[i]:
			if letter not in letterCount:
				letterCount[letter] = 1
			else:
				letterCount[letter] += 1
		
		for j in range(0, len(words)):
			if words[j] == words[i]:
				continue
			secondLetterCount = {}
			for letter in words[j]:
				if letter not in secondLetterCount:
					secondLetterCount[letter] = 1
				else:
					secondLetterCount[letter] += 1
			if letterCount == secondLetterCount:
				sub.append(words[j])
				
		
		sub.sort()
		print(sub)
		if sub not in result:
			result.append(sub)
		
	return result