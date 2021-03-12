# # Problem statement:

# Design and code a multi-shelf, smart bookcase that supports the following requests:
# 1. What is the Nth book, ignoring shelving divisions?
# 2. Where is the book named X located(shelf and position)?
# 3. What is the name of the next/previous book after/before the book named X?

# Input:
# - The dimensions of the bookcase, as a 1-D array or list, ordered top to bottom(Rows: Amount of shelves, Column: Amount of books each shelf can hold)
# - A list of the titles of enough books to perfectly fill the bookcase(Assume all books are the same physical size)


# bookcase_dimensions = [3, 4] // 3 Rows with each row having space for 4 books of dimension/size 1

# book_titles = ["AA", "AB", "C", "CD", "E",
#                "FF", "Q", "T", "TT", "V", "VY", "ZZZ"]

# Things to consider:
# - Object oriented programming
# - Develop a solution that supports all requests, as opposed to 3 separate solutions

# # Notes, design & assumptions

# #input = [3, 4]
# # _ _ _ _
# # _ _ _ _
# # _ _ _ _

# requests:
# 1. getNth(n) = > getNth(5) = > E
# 2. getlocation(bookName) = > getlocation("FF") = > [1, 1]
# 3. getNext(bookName) = > getNext("FF") = > Q
# 4. getPrev(bookName) = > getNext("FF") = > E

# AA AB C CD
# E  FF Q T
# TT V VY ZZZ

# design:

class BookCase:
    def __init__(self, rows, cols, bookTitles):
        self.rows = rows
        self.cols = cols
        self.bookCase = [[None] * self.cols for _ in range(self.rows)]

        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if len(bookTitles) > 0:
                    self.bookCase[row][col] = bookTitles.pop(0)

    def getNthBook(self, n):
        steps = n
        for row in range(len(self.bookCase)):
            for col in range(len(self.bookCase[0])):
                steps -= 1
                if steps == 0:
                    return self.bookCase[row][col]

    def getLocation(self, bookName):
        for row in range(len(self.bookCase)):
            for col in range(len(self.bookCase[0])):
                if self.bookCase[row][col] == bookName:
                    return [row, col]

        return False

    def getNext(self, bookName):
        for row in range(len(self.bookCase)):
            for col in range(len(self.bookCase[0])):
                if self.bookCase[row][col] == bookName:
                    if col < (len(self.bookCase[0]) - 1):
                        return self.bookCase[row][col+1]
                    else:
                        if row == len(self.bookCase) - 1:
                            return False
                        else:
                            return self.bookCase[row+1][0]


# bookcase_dimensions = [ 3, 4] #3 Rows with each row having space for 4 books of dimension/size 1
book_titles = ["AA", "AB", "C", "CD", "E",
               "FF", "Q", "T", "TT", "V", "VY", "ZZZ"]

# ["AA", "AB", "C", "CD",
# "E", "FF", "Q", "T",
# "TT", "V", "VY", "ZZZ"]

bookCase = BookCase(3, 4, book_titles)
print(bookCase.getNext("ZZZ"))
