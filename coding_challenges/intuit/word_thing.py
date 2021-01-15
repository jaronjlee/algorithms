import sys
import math

# Prints to standard output.


def reflowLines(line_length, lines):
  words = []
  result = []

  for line in lines:
    words += line.split()

  tempLine = []
  tempNewLine = []
  for word in words:
    tempNewLine.append(word)

    if calculateLength(tempNewLine) <= line_length:
      tempLine.append(word)
      continue
    else:
      result.append(justifyLine(tempLine, line_length))
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
  numHyphensPerSlot = emptySlots / spaces
  numCeilingSpaces = emptySlots % spaces

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
