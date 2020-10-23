def playSegments(coins):
    # Write your code here
    length = len(coins)
    total = 0
    
    for coin in coins:
        if coin == 1:
            total += 1
        elif coin == 0:
            total -= 1
    
    p1 = 0
    p2 = total
    
    for i in range(len(coins)):
        if p1 > p2:
            return i
        
        if coins[i] == 1:
            p1 += 1
            p2 -= 1
        elif coins[i] == 0:
            p1 -= 1
            p2 += 1
    