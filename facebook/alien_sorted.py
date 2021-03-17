class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # return True if word1 is less than word2 in lexicographical order
        def compareWords(word1, word2, letterIndices):
            if word1 == word2:
                return True

            i = 0
            while i < len(word1) and i < len(word2):
                letterOneIndex = letterIndices[word1[i]]
                letterTwoIndex = letterIndices[word2[i]]
                if letterOneIndex < letterTwoIndex:
                    return True
                elif letterOneIndex > letterTwoIndex:
                    return False
                i += 1

            if len(word1) < len(word2):
                return True
            else:
                return False

        if len(words) == 1:
            return True

        letterIndices = {}

        for i in range(0, len(order)):
            letterIndices[order[i]] = i

        for i in range(0, len(words)-1):
            currWord = words[i]
            nextWord = words[i+1]
            if compareWords(currWord, nextWord, letterIndices) == False:
                return False

        return True
