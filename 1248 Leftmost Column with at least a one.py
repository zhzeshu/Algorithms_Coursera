
# funcamental methods, won't pass

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        col_smallest = col
        for i in range(row):
            for j in range(col):
                if binaryMatrix.get(i, j) == 1:
                    col_smallest = min(col_smallest, j)
                    break
        if col_smallest == col:
            return -1
        else:
            return col_smallest