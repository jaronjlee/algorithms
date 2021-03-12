def moves(arr):
    left = 0
    right = len(arr)-1
    moves = 0
    while left < right:
        while arr[left] % 2 == 0:
            left += 1
        while arr[right] % 2 != 0:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            moves += 1
            left += 1
            right -= 1
    return moves
