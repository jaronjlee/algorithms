#find min number of moves from start pos to end pos
#can move in the directions of a knight (2 and then 1)
#n is size of the board


# n = 5

#   0 1 2 3 
# 0 _ _ _ _ 
# 1 _ _ _ _ 
# 2 _ _ _ _ 
# 3 S _ E _ 

# queue = [[3,0]]
# length = 1
# pos = [3,0]
# newPos = 



def minMoves(n, startRow, startCol, endRow, endCol):
    visited = [[False] * n for _ in range(n)]
    visited[pos[0]][pos[1]] = True
    count = 0
    queue = [[startRow, startCol]]

    while queue:
        numChecks = len(queue)
        for 0 in range(numChecks):
            pos = queue.pop
            for x,y in [(2,1), (-2,1), (2,-1), (-2,-1), (1,2), (1,-2),(-1,2),(-1,-2)]:
                newX = pos[0] + x
                newY = pos[1] + y
                if newX >= 0 and newX < n and newY >= 0 and newY < n and visited[newX][newY] == False:
                    if newX == endRow and newY == endCol:
                        return count += 1
                    queue.append([newX,newY])
                    visited[newX][newY] = True
        count += 1
    
    return -1

