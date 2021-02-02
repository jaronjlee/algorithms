#Time Complexity O(lines * maxWidth)
#for every line that we have, we are going to iterate to maxWidth
#Space Complexity O(lines * maxWidth)

import sys
import math

def reflowLines(line_length, lines): #given 2D array of lines where each line is an array
  words = []
  result = []

  for line in lines:                #get an array of just words
    words += line.split()

  tempLine = []                      #tempLine is the array we run through justifyLine helper function
  tempNewLine = []                    #tempNewLine is array where we test if next word puts us over the line_length
  for word in words:                
    tempNewLine.append(word)

    if calculateLength(tempNewLine) <= line_length: #if adding the next word doesnt put us over, we add the next word to templine
      tempLine.append(word)
      continue
    else:
      result.append(justifyLine(tempLine, line_length)) #if it does, then we just keep tempLine and justify it. then reset tempLine and tempNewLine to the current word
      tempLine = [word]
      tempNewLine = [word]

  if len(tempLine) == 1:
    result += tempLine
  elif len(tempLine) > 1:
    result.append(justifyLine(tempLine, line_length))

  for line in result:
    print(line)


def calculateLength(wordsArray):
  line = "-".join(wordsArray)
  return len(line)


def justifyLine(line, line_length):
  if len(line) == 1:
    return line[0]

  result = ""

  chars = 0
  for word in line:
    chars += len(word)

  spaces = len(line)-1
  emptySlots = line_length - chars
  numHyphensPerSlot = emptySlots / spaces   #num empty slots / spaces returns a float. float.floor or float.ceil determines num hyphens
  numCeilingSpaces = emptySlots % spaces    #number of math.ceiling spots are needed if emptyslots % spaces > 0. 

  if numCeilingSpaces == 0:
    hyphens = "-" * int(numHyphensPerSlot)
    return hyphens.join(line)
  else:
    justifiedWord = ""
    countCeilingSpaces = numCeilingSpaces
    for i in range(0, spaces):
      word = line[i]
      if countCeilingSpaces > 0:
        justifiedWord += word + "-" * math.ceil(numHyphensPerSlot)
        countCeilingSpaces -= 1
      else:
        justifiedWord += word + "-" * math.floor(numHyphensPerSlot)

    result = justifiedWord + line[-1]

  return result


# DO NOT MODIFY BELOW THIS LINE
def main():
  first_line = None
  lines = []

  first_arg = True
  for line in sys.stdin:
    if len(line.strip()) == 0:
      continue

    line = line.rstrip()

    if first_arg:
      lineLength = int(line)
      first_arg = False
    else:
      lines.append(line)

  reflowLines(lineLength, lines)


main()
