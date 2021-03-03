#design a hospital waiting room that can insert and remove patients from a queue
#if at max capacity, dont accept anymore patients
#add weights for people who are more injured to get admitted first

#number represents a patient
#lower the number, the higher the priority

#priority queue in the form of a min heap (binary tree)
#every parent node is <= its child nodes
#insert: append node to end of the array, then sift value up the tree until reaches its position
#remove: swap first and last ele in array, then sift first ele down. return last ele popped off


#     1
#   5.  3
# 4.  2


# [1, 5, 3, 4, 2]
#  0  1. 2. 3. 4.

# currentIdx = n
# parentIdx = (n - 1) // 2
# childOne = (n * 2) + 1
# childTwo = (n * 2) + 2

#threads
#raise errors

import heapq

class WaitingRoom:
  def __init__(self, maxSize):
    self.maxSize = maxSize
    self.currentSize = 0
    self.queue = []  # right to left

  def insert(self, patient):  # raise TypeError
    if type(patient) != int or patient < 1:
      raise TypeError("input must be a positive integer")

    if self.currentSize < self.maxSize:
      self.queue.append(patient)
      self.currentSize += 1
      self.siftUp(len(self.queue)-1, self.queue)
    else:
      print("waiting room is full")

  def remove(self):
    self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
    valueToRemove = self.queue.pop()
    self.currentSize -= 1
    self.siftDown(0, len(self.queue) - 1, self.queue)
    return valueToRemove

  def peak(self):
    return self.queue[0]

  def siftUp(self, currentIdx, queue):
    parentIdx = (currentIdx - 1) // 2
    while parentIdx >= 0:
      if queue[currentIdx] < queue[parentIdx]:
        queue[currentIdx], queue[parentIdx] = queue[parentIdx], queue[currentIdx]
        currentIdx = parentIdx
        parentIdx = (currentIdx - 1) // 2
      else:
        break

  def siftDown(self, currentIdx, lastIdx, queue):
    childOneIdx = (currentIdx * 2) + 1
    while childOneIdx <= lastIdx:
      childTwoIdx = (currentIdx * 2) + 2
      idxToSwap = None
      if childTwoIdx <= lastIdx and queue[childTwoIdx] < queue[childOneIdx]:
        idxToSwap = childTwoIdx
      else:
        idxToSwap = childOneIdx
      if queue[idxToSwap] < queue[currentIdx]:
        queue[idxToSwap], queue[currentIdx] = queue[currentIdx], queue[idxToSwap]
        currentIdx = idxToSwap
        childOneIdx = (currentIdx * 2) + 1
      else:
        break


# waitingRoom = WaitingRoom(10)
# waitingRoom.insert(5)
# waitingRoom.insert(2)
# waitingRoom.insert(3)
# waitingRoom.insert(4)
# print(waitingRoom.remove()) #remove 2
# waitingRoom.insert(7)
# waitingRoom.insert(1)
# print(waitingRoom.remove()) #remove 1
# print(waitingRoom.queue)
# print(waitingRoom.peak()) #3

class WaitingRoom2:
  def __init__(self):
    self.heap = []
    heapq.heapify(self.heap)

  def insert(self, ele):
    heapq.heappush(self.heap, ele)

  def remove(self):
    return heapq.heappop(self.heap)


waitingRoom = WaitingRoom2()
waitingRoom.insert(3)
waitingRoom.insert(5)
waitingRoom.insert(2)
waitingRoom.insert(1)
print(waitingRoom.heap)
print(waitingRoom.remove())
print(waitingRoom.remove())
print(waitingRoom.remove())
print(waitingRoom.heap)
