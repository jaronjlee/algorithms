def convert_roman_numeral(roman_numeral):
  hash = {
    "I":1,
    "II":2,
    "III":3,
    "IV":4,
    "V":5,
    "VI":6,
    "VII":7,
    "VIII":8,
    "IX":9,
    "X":10,
    "XX":20, 
    "XXX":30, 
    "XL":40,
    "L":50
  }

  if len(roman_numeral) == 1:
    return hash[roman_numeral]
  
  result = 0

  i = 0
  while i < len(roman_numeral):
    if i < len(roman_numeral)-1 and hash[roman_numeral[i]] < hash[roman_numeral[i+1]]:
      current_letter = roman_numeral[i]
      next_letter = roman_numeral[i+1]
      num = hash[next_letter]-hash[current_letter]
      result += num
      i += 2
    else:
      result += hash[roman_numeral[i]]
      i += 1

  return result


def get_bigger_name(name1, name2):
  name1_arr = name1.split(" ")
  name2_arr = name2.split(" ")

  first_name1 = name1_arr[0]
  first_name2 = name2_arr[0]

  roman1 = name1_arr[1]
  roman2 = name2_arr[1]

  roman1_number = convert_roman_numeral(roman1)
  roman2_number = convert_roman_numeral(roman2)

  if first_name1 != first_name2:
    return max(name1, name2) 
  
  if roman1_number > roman2_number:
    return name1
  else:
    return name2


names = ["Steven XL", "Steven XVI", "David IX", "Mary XV", "Mary XIII", "Mary XX"]

def quick_sort(arr):
  if len(arr) < 1:
    return arr

  pivot = arr[0]
  left = []
  right = []

  for i in range(1, len(arr)):
    if get_bigger_name(pivot, arr[i]) == pivot:
      left.append(arr[i])
    else:
      right.append(arr[i])

  sorted_left = quick_sort(left)
  sorted_right = quick_sort(right)
  
  return sorted_left + [pivot] + sorted_right

print(quick_sort(names))