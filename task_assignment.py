from collections import defaultdict


def taskAssignment(k, tasks):
    taskIndices = defaultdict(list)


for i in range(0, len(tasks)):
		taskIndices[tasks[i]].append(i)

	tasks.sort()
	result = []

	i = 0
	j = len(tasks)-1

	while i < j:
		leftIdx = taskIndices[tasks[i]].pop(-1)
		rightIdx = taskIndices[tasks[j]].pop(-1)
		result.append([leftIdx, rightIdx])
		i += 1
		j -= 1

	return result

# def taskAssignment(k, tasks):
#     taskIndices = []

# 	for i in range(0, len(tasks)):
# 		taskIndices.append([tasks[i], i])

# 	taskIndices.sort()

# 	result = []

# 	i = 0
# 	j = len(taskIndices)-1

# 	while i < j:
# 		leftIdx = taskIndices[i][1]
# 		rightIdx = taskIndices[j][1]
# 		result.append([leftIdx, rightIdx])
# 		i += 1
# 		j -= 1

# 	return result
