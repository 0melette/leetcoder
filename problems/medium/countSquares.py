from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        total_squares = 0

        countTable = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 1:
                    if row == 0 or col == 0:
                        countTable[row][col] = 1
                    else:
                        countTable[row][col] = 1 + min(
                            countTable[row-1][col], # up
                            countTable[row][col-1], # left
                            countTable[row-1][col-1] # up left
                        )
                    total_squares += countTable[row][col]

        return total_squares
