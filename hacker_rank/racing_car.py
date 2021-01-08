# def minimumMovement(obstacleLanes):
#     count = 0
#     currentLane = 2
#     i = 0
#     while i < len(obstacleLanes)-2:
#         firstObstacle = obstacleLanes[i]
#         secondObstacle = obstacleLanes[i+1]
#         thirdObstacle = obstacleLanes[i+2]
#         obstacles = [firstObstacle, secondObstacle, thirdObstacle]
#         if firstObstacle != currentLane:
#             i += 1
#         elif currentLane == firstObstacle == secondObstacle == thirdObstacle:
#             i += 2
#         elif firstObstacle == currentLane:
#             if 2 not in obstacles:
#                 count += 1
#                 currentLane = 2
#                 i += 3
#             elif 1 not in obstacles:
#                 count += 1
#                 currentLane = 1
#                 i += 3
#             elif 3 not in obstacles:
#                 count += 1
#                 currentLane = 3
#                 i += 3
#             else:  # if 1 2 and 3 are in obstacles array
#                 count += 1
#                 currentLane = thirdObstacle
#                 i += 2
#     print(count)
#     print(i)
#     print(len(obstacleLanes)-1)
#     if i == len(obstacleLanes)-1 and obstacleLanes[i] == currentLane:
#         return count + 1
#     else:
#         return count

['', float('inf'), '']
['', '', float('inf')]
['', float('inf'), '']
[1,      0,         1

#check value underneath
#if inf under, make it 2
#if 1 under, make it 1
#if next possible row == '' and prevRowPos == 'inf', change row to min of prev row + 1
#if next possible row is '' and prevRowPos != 'inf', change pos to the prev row pos
#each space is the min number of moves it takes to get to that space
#if below is an 'inf', change current pos to min value of the value of the row beneath 
#return min of the top row of the grid

def minimumMovement(obstacleLanes):
    #create grid
    carRows = ['','',''] * len(obstacleLanes)
    
    #loop over nested arrays to add obstacles

    #
    return carRows