class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        SR = 0
        ER = len(matrix)-1
        SC = 0
        EC = len(matrix[0])-1

        while SR <= ER and SC <= EC:

            #left to right
            for col in range(SC, EC+1):
                result.append(matrix[SR][col])

            #top right to bottom right
            for row in range(SR+1, ER+1):
                result.append(matrix[row][EC])

            #bottom right to bottom left
            for col in range(EC-1, SC-1, -1):
                if SR == ER:
                    break
                result.append(matrix[ER][col])

            #bottom left to top left
            for row in range(ER-1, SR, -1):
                if SC == EC:
                    break
                result.append(matrix[row][SC])

            SR += 1
            SC += 1
            EC -= 1
            ER -= 1

        return result
