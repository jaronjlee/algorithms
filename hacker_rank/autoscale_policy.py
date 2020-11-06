def finalInstances(instances, averageUtil):
    # Write your code here
    
    if len(averageUtil) == 0:
        return instances
    
    i = 0
    while i < len(averageUtil):
        if averageUtil[i] in range(0, 25) and instances > 1:
            instances = math.ceil(instances/2)
            i += 11
        elif averageUtil[i] > 60 and instances * 2 <= 2*(10**8):
            instances = instances * 2
            i += 11
        else:
            i += 1

    return instances