#there are n people standing in a queue for bus numbered from left to right, 1 to n

def kthPerson(k, p, q):
    # Write your code here
    result = []
    
    for arrivalTime in q:
        if len(p) < 1:
            result.append(0)
            continue
        
        lastPassenger = 0
        i = 0
        while i < k and len(p) > 0:
            if p[0] < arrivalTime:
                p.pop(0)
            elif p[0] >= arrivalTime:
                lastPassenger = p.pop(0)
                i += 1

        result.append(lastPassenger)
        
    return result


