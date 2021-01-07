def minimumMovement(obstacleLanes):
    count = 0
    currentLane = 2
    i = 0
    while i < len(obstacleLanes)-2:
        firstObstacle = obstacleLanes[i]
        secondObstacle = obstacleLanes[i+1]
        thirdObstacle = obstacleLanes[i+2]
        obstacles = [firstObstacle, secondObstacle, thirdObstacle]
        if firstObstacle != currentLane:
            i += 1
        elif firstObstacle == currentLane:
            if
            if 2 not in obstacles:
                count += 1
                currentLane = 2
                i += 3
            elif 1 not in obstacles:
                count += 1
                currentLane = 1
                i += 3
            elif 3 not in obstacles:
                count += 1
                currentLane = 3
                i += 3
            else:  # if 1 2 and 3 are in obstacles array
                count += 1
                currentLane = thirdObstacle
                i += 2
    print(count)
    print(i)
    print(len(obstacleLanes)-1)
    if i == len(obstacleLanes)-1 and obstacleLanes[i] == currentLane:
        return count + 1
    else:
        return count
