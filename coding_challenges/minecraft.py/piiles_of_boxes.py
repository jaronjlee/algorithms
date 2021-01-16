def minSteps(piles):
  if len(piles) < 1:
    return 0

  piles.sort()

  steps = 0
  distinctNums = 0
  for i in range(1, len(piles)):
    print(piles[i])
    print(piles[i-1])
    if piles[i] == piles[i-1]:
      steps += distinctNums
    else:
      distinctNums += 1
      steps += distinctNums

  return steps


# x = [5, 3, 2]
# y = [5, 5, 3, 2]
# z = [6, 6, 5, 5, 2, 1]
# a = [3, 2, 1] 

