def minimumWaitingTime(queries):
    minTime = 0


queries.sort()

for i in range(0, len(queries)):
		queriesLeft = len(queries) - 1 - i
		print(queriesLeft)
		print(queries[i])
		minTime += queriesLeft*queries[i]

	return minTime
