# Write a function that takes in a list of (student ID number, course name) pairs
# and returns, for every pair of students, a list of all courses they share.

# Sample Input:
# student_course_pairs = [
#   ["58", "Software Design"],
#   ["58", "Linear Algebra"],
#   ["94", "Art History"],
#   ["94", "Operating Systems"],
#   ["17", "Software Design"],
#   ["58", "Mechanics"],
#   ["58", "Economics"],
#   ["17", "Linear Algebra"],
#   ["17", "Political Science"],
#   ["94", "Economics"]
# ]

# Sample Output (pseudocode, in any order)

# find_pairs(student_course_pairs) =>
# {
#     [58, 17]: ["Software Design", "Linear Algebra"]
#     [58, 94]: ["Economics"]
#     [17, 94]: []
# }  

# [58, 17, 94]

from collections import defaultdict


def findPairs(student_course_pairs):
  studentCourses = defaultdict(set)
  courses = set()
  students = set()
  result = {}

  for student, course in student_course_pairs:
    studentCourses[student].add(course)
    courses.add(course)
    students.add(student)

  studentsArr = list(students)
  # print(studentCourses)
  # print(studentsArr)

  for i in range(0, len(studentsArr)-1):
    for j in range(i+1, len(studentsArr)):
      student1 = studentsArr[i]
      student2 = studentsArr[j]
      pair = str([student1, student2])
      result[pair] = []
      for course in courses:
        if course in studentCourses[student1] and course in studentCourses[student2]:
          result[pair].append(course)

  return result


student_course_pairs = [
    ["58", "Software Design"],
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"]
]

print("hello")
print(findPairs(student_course_pairs))
