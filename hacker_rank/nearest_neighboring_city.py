def closestStraightCity(c, x, y, q):
    # Write your code here
    result = []
    
    for i in range(0, len(q)):
        
        closest = "NONE"
        distance = float("inf")
        
        for j in range(0, len(c)):
            if i != j:
                if x[i] == x[j]:
                    new_distance = abs(y[i] - y[j])
                    if new_distance < distance:
                        distance = new_distance
                        closest = c[j]
                    elif new_distance == distance:
                        closest = min(c[j].lower(), closest.lower())
                elif y[i] == y[j]:
                    new_distance = abs(x[i] - x[j])
                    if new_distance < distance:
                        distance = new_distance
                        closest = c[j]
                    elif new_distance == distance:
                        closest = min(c[j].lower(), closest.lower())
            
        result.append(closest)
                
    return result