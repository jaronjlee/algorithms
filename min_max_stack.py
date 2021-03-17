class MinMaxStack:
	def __init__(self):
		self.stack = []
		self.minMaxStack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.minMaxStack.pop()
		return self.stack.pop()

    def push(self, number):
        if len(self.stack) == 0:
			newMinMax = {"min": number, "max": number}
			self.minMaxStack.append(newMinMax)
		else:
			lastMinMax = self.minMaxStack[len(self.minMaxStack)-1]
			newMinMax = {
				"min": min(number, lastMinMax["min"]),
				"max": max(number, lastMinMax["max"])
			}
			self.minMaxStack.append(newMinMax)
		self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[-1]["min"]

    def getMax(self):
        return self.minMaxStack[-1]["max"]
