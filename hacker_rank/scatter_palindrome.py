from collections import defaultdict


def scatterPalindrome(strToEvaluate):
    count = defaultdict(int)
    for string in strToEvaluate:
        for i in range(0, len(string)):
            for j in range(i+1, len(string)+1):
                substring = string[i:j]
                if possiblePalindrome(substring):
                    count[string] += 1
    return list(count.values())


def possiblePalindrome(str):
    count = defaultdict(int)
    sortedStr = sorted(str)
    one = False
    for i in range(0, len(sortedStr)):
        char = sortedStr[i]
        count[char] += 1
        if i > 0:
          prev = sortedStr[i-1]
          if char != prev and count[prev] == 1:
            if not one:
              one = True
            else:
              return False
          if char != prev and count[prev] > 1 and count[prev] % 2 != 0:
            return False
    values = list(count.values())
    ones = 0
    odds = 0
    for count in values:
        if count == 1:
            ones += 1
            continue
        elif count % 2 != 0:
            odds += 1
    if ones > 1:
        return False
    elif ones == 1 and odds > 0:
        return False
    return True
