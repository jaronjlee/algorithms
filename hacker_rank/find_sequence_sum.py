#given three integers, i, j, and k, a sequence sum to be the value of i + (i + 1)...


def getSequenceSum(i, j, k):
    result = 0
    up = j - i #2
    down = j - k #4
    # test = []
    
    increment = 0
    while increment <= up:
        if increment >= up - down and i + increment < j:
            result += (i + increment) * 2
            # test.append(i + increment)
            # test.append(i + increment)
            # print((i + increment))
            # print((i + increment))
        else:
            result += (i + increment)
            # test.append(i + increment)
            # print((i + increment))
            
        increment += 1
        
    print(increment)
    extraDecrement = i - 1
    count = 0
    if down > up:
        while count < down - up:
            result += extraDecrement
            # test.append(extraDecrement)
            extraDecrement -= 1
            count += 1
            

        
    # print(test)
    return result