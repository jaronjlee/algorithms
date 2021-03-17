from collections import defaultdict


def generateDocument(characters, document):
    requiredCount = defaultdict(int)


actualCount = defaultdict(int)

for char in document:
		requiredCount[char] += 1

	for char in characters:
		actualCount[char] += 1

	for key in requiredCount:
		if actualCount[key] < requiredCount[key]:
			return False

	return True
