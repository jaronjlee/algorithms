def countPairs(numbers, k):
    count = 0
    seenPairs = set()
    numbers = sorted(list(set(numbers)))
    left = 0
    right = 0

    while right < len(numbers):
        currentSum = numbers[right] - numbers[left]
        if currentSum == k:
            count += 1
            left += 1
            right += 1
        elif currentSum < k:
            right += 1
        else:
            left += 1

    return count
