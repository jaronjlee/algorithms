# An ideal number is a positive integer that has only 3 and 5 as prime divisors. 
# An ideal number can be expressed in the form of 3^x * 5^y, where x and y are non-negative integers. 
# For example, 15, 45 and 75 are ideal numbers but 6, 10, 21 are not. 
# Find the number of ideal integers within the given segment[low, high] inclusive.

# example:
# low = 200
# high = 405

# power   of 3    of 5
# 0       1       1
# 1       3       5
# 2       9       25
# 3       27      125
# 4       81      625
# 5       243     3125
# 6       729     15625

# there are 4 ideal integers in the range of [200, 405] inclusive:
# 3^2 * 5^2 = 9 * 25 = 225
# 3^5 * 5^0 = 243 * 1 = 243
# 3^1 * 5^3 = 3 * 125 = 375
# 3^4 * 5^1 = 81 * 5 = 405


def getIdealNums(lower, upper):
    powers = []

    start = None
    if lower % 2 == 0:
      start = lower + 1
    else:
      start = lower

    for i in range(start, upper+1, 2):
        if i % 3 == 0 or i % 5 == 0:
            powers.append(i)

    count = 0
    for num in powers:
        temp = num
        while temp % 3 == 0:
            temp /= 3

        while temp % 5 == 0:
            temp /= 5

        if temp == 1:
            count += 1

    return count


print(getIdealNums(200, 405))


# def getIdealNums(lower, upper):
    
#     count = 0
#     for i in range(lower, upper+1):
#         num = i
#         while num % 3 == 0:
#             num /= 3

#         while num % 5 == 0:
#             num /= 5

#         if num == 1:
#             count += 1

#     return count

print(getIdealNums(200, 405))
