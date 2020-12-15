def getUmbrellas(n, denoms):
    # Write your code here.

    mins = [float("inf")] * (n+1)
    mins[0] = 0

    for denom in denoms:
        for i in range(0, len(mins)):
            if denom <= i:
                mins[i] = min(mins[i], mins[i-denom] + 1)

    return mins[n] if mins[i] != float("inf") else -1
