def efficientJanitor(weight):
    # Write your code here
    trips = 0
    i = 0
    running_total = 0
    while i < len(weight):
        running_total = weight[i]
        j = i+1
        while j < len(weight):
            if running_total + weight[j] <= 3.00:
                running_total += weight[j]
                j += 1
            else:
                break
        trips += 1
        i = j
    
    return trips