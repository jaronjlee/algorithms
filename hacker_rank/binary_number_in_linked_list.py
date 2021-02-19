def getNumber(binary):
    node = binary
    binaryDigits = []
    result = 0

    while node is not None:
        binaryDigits.append(node.data)
        node = node.next

    # print(binaryDigits)

    i = len(binaryDigits)-1
    power = 0
    while i >= 0:
        binaryDigit = binaryDigits[i]
        if binaryDigit == 1:
            result += (2**power)

        power += 1
        i -= 1

    return result
