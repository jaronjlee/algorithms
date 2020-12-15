#other way
# [1, 2, 3, 4, 3, 2, 3, 2, 1]
#two arrays, representing the monster at each ends blow counts to reach each index of the given array
#from the left you get [1, 1, 1, 1, 2, 3, 3, 4, 5]
#from the right you get [5, 4, 3, 2, 2, 2, 1, 1, 1]
#find the minimum sum at each intersection point, return the min overall


def getMinimumBlows(height):
    # Write your code here
    if len(height) < 3:
        return 1
    
    count = 0
    
    l = 0
    r = len(height)-1
    
    while l < r:
        tl = l
        tr = r
        
        if tl < len(height) and height[tl+1] > height[tl]:
            tl += 1
                
        if tr >= 0 and height[tr-1] > height[tr]:
            tr -= 1
                
        leftMoves = tl - l
        rightMoves = r - tr
        
        print(leftMoves)
        print(rightMoves)
 
        if leftMoves >= rightMoves:
            l += leftMoves
            count += 1
        elif rightMoves > leftMoves:
            r -= rightMoves
            count += 1
        elif rightMoves == 0 and leftMoves == 0:
            count += 2
            l += 1
            r -= 1
            
    return count


print(getMinimumBlows([1, 2, 3, 4, 3, 2, 3, 2, 1]))


