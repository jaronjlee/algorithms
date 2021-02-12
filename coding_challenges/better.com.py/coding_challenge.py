#1
def solution(N):
    numStr = str(N)
    numStrArr = []
    for char in numStr:
        numStrArr.append(char)

    if N >= 0:
        for i in range(0, len(numStr)):
            currentDigit = int(numStr[i])
            if 5 > currentDigit:
              numStrArr.insert(i, "5")
              break
            if i == len(numStr)-1:
              numStrArr.insert(i, "5")

    if N < 0:
        for i in range(1, len(numStr)):
            currentDigit = int(numStr[i])
            if 5 < currentDigit:
                numStrArr.insert(i, "5")
                break

    return int("".join(numStrArr))



#2
def solution(S):
    result = float("inf")
    for i in range(0, len(S)):
        for j in range(i+1, len(S)+1):
            subString = S[i:j]
            if balancedString(subString):
                result = min(j-i, result)

    if result == float("inf"):
        return -1
    else:
        return result


def balancedString(s):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper = [False]*26
    lower = [False]*26

    for char in s:
        index = alpha.index(char.upper())
        if char.upper() == char:
            upper[index] = True
        else:
            lower[index] = True

    for i in range(26):
        if upper[i] != lower[i]:
            return False

    return True


#3
def solution(S, K):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    startIdx = None
    for i in range(0, len(days)):
        if S == days[i]:
            startIdx = i
            break

    steps = K % 7
    currentIdx = startIdx
    while steps > 0:
        currentIdx += 1
        if currentIdx == 7:
            currentIdx = 0
        steps -= 1

    return days[currentIdx]
