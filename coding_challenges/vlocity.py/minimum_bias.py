#array of ratings, difference between a pair or ratings is a bias
#find total minimum bias
#assume length of array is even

def minimumBias(ratings):
  totalBias = 0
  ratings.sort()
  for i in range(0, len(ratings), 2):
    totalBias += (ratings[i+1]-ratings[i])

  return totalBias


# ratings = [4, 2, 5, 1]
ratings = [1, 3, 6, 6]
print(minimumBias(ratings))
