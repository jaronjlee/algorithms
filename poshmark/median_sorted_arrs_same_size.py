def medianOfSortedArrays(A, B):
  if A[-1] <= B[0]:
    return (B[0] + A[-1]) / 2
  elif B[-1] <= A[0]:
    return (A[0] + B[-1]) / 2

  totalLength = len(A) + len(B)
  mid1 = (totalLength / 2)-1
  mid2 = mid1 + 1

  moves = 0
  i = 0
  j = 0

  m1 = None
  m2 = None

  while moves <= mid2:
    if moves == mid1:
      m1 = min(A[i], B[j])
    if moves == mid2:
      m2 = min(A[i], B[j])

    if A[i] <= B[j]:
      i += 1
      moves += 1
    else:
      j += 1
      moves += 1

  return (m1 + m2) / 2


# 1 2 3 4 5 6 7 8
a = [1, 3, 4, 8]
b = [2, 5, 6, 7]

print(medianOfSortedArrays(a, b))



# O(log n) Time
# def findMedianSortedArrays(A, B):
#        if len(A) > len(B):
#             return findMedianSortedArrays(B, A)

#         lenA = len(A)
#         lenB = len(B)

#         #find partition for arr A
#         low = 0
#         high = lenA

#         while low <= high:
#             partitionA = (low + high) // 2
#             partitionB = (lenA + lenB + 1) // 2 - partitionA

#             maxLeftA = float("-inf") if partitionA == 0 else A[partitionA-1]
#             minRightA = float("inf") if partitionA == lenA else A[partitionA]
#             maxLeftB = float("-inf") if partitionB == 0 else B[partitionB-1]
#             minRightB = float("inf") if partitionB == lenB else B[partitionB]

#             if maxLeftA <= minRightB and maxLeftB <= minRightA:
#                 if (lenA + lenB) % 2 == 0:
#                     mid1 = max(maxLeftA, maxLeftB)
#                     mid2 = min(minRightA, minRightB)
#                     return (mid1 + mid2) / 2
#                 else:
#                     return max(maxLeftA, maxLeftB)
#             elif maxLeftA > minRightB:
#                 high -= 1
#             elif maxLeftB > minRightA:
#                 low += 1
