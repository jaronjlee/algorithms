from collections import defaultdict


def getUniqueCharacter(s):
    count = defaultdict(int)
    for char in s:
        count[char] += 1
    for i in range(0, len(s)):
        if count[s[i]] == 1:
            return i + 1
    return -1
