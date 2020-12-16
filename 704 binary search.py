def binary_search(arr, target):
    left, right = 0, len(arr) -1
    while left <= right:
        middle = left + (right-left)//2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle -1

    return -1


print(binary_search([-1, 0, 1, 3, 4, 5, 6], 5))


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        col_smallest = col
        for i in range(row):
            left = 0
            right = col - 1
            while left < right:
                middle = left + (right - left) // 2
                if binaryMatrix.get(i, middle) == 0:
                    left = middle + 1
                else:
                    right = middle

            if binaryMatrix.get(i, left) == 1:
                col_smallest = min(col_smallest, left)

        if col_smallest == col:
            return -1
        else:
            return col_smallest


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        current_row = 0
        current_col = col - 1
        while current_row < row and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 0:
                current_row += 1
            else:
                current_col -= 1

        if current_col != col - 1:
            return current_col + 1
        else:
            return -1
