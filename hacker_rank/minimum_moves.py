def minimumMoves(arr1, arr2):
    # Write your code here
    moves = 0
    for i in range(0, len(arr1)):
        num1 = arr1[i]
        num2 = arr2[i]
        moves += compare(num1, num2)
    
    return moves
    
# 24
# 45

# 24 % 10 = 4
# 24 // 10 ==
        
def compare(num1, num2):
    moves = 0
    while num1 > 0 and num2 > 0:
        digit1 = num1 % 10
        digit2 = num2 % 10
        # print(digit1)
        # print(digit2)
        diff = abs(abs(num1)-abs(num2))
        moves += diff
        num1 = num1//10
        num2 = num2//10

    return moves