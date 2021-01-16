import string


def howMany(sentence):
    wordsArr = sentence.split()
    count = 0
    for word in wordsArr:
        if validWord(word):
            count += 1
    return count


def validWord(word):
    alpha = string.ascii_letters
    alpha += "-,.?!"
    alphaSet = set()
    for letter in alpha:
        alphaSet.add(letter)
    for letter in word:
        if letter not in alphaSet:
            return False
    return True
