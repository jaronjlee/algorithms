def coprimeCount(A):
    result = []

    for num in A:
        count = 0
        if num == 1:
            result.append(1)
            continue

        for i in range(1, num):
            if gcd(i, num) == 1:
                count += 1

        result.append(count)

    return result


def gcd(a, b):
    if not b:
        return a

    return gcd(b, a % b)
