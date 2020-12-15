def minSwaps(popularity):
    numSwaps = 0
    i = 0
    while i < len(popularity):
        diff = len(popularity) - popularity[i]
        if diff == i:
            i+=1
            continue
        popularity[diff], popularity[i] = popularity[i], popularity[diff]
        numSwaps+=1
    return numSwaps