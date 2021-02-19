def getUmbrellas(requirement, sizes):
    mins = [float("inf")] * (requirement+1)

    for size in sizes:
        for i in range(0, len(mins)):
            if i < size:
                continue
            if size == i:
                mins[i] = 1
                continue
            diff = i - size
            mins[i] = min(mins[diff] + 1, mins[i])

    if mins[-1] == float("inf"):
        return -1
    else:
        return mins[-1]
