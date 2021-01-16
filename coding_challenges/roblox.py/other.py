
from collections import Counter

#find minimum unique elements bag can contain after removing allowed number of items

def deleteProducts(ids, m):
    countHash = {}
    for id in ids:
        if id not in countHash:
            countHash[id] = 0
        countHash[id] += 1

    arr = []
    for id in sorted(countHash, key=countHash.get, reverse=False):
        for i in range(0, countHash[id]):
            arr.append(id)

    leftToRemove = m
    while leftToRemove > 0 and len(arr) > 0:
        arr.pop(0)
        leftToRemove -= 1

    unique = Counter(arr).keys()
    return len(unique)
