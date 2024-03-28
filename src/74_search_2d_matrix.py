from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)
        while l < r:
            m = (l + r) // 2
            left = matrix[l:m]
            right = matrix[m:r]
            if left and target > max(left)[-1]:
                l = m
            if right and target < min(right)[0]:
                r = m
            if len(left) == 1 and target in left[0]:
                return True
            if len(right) == 1 and target in right[0]:
                return True
            if len(left) <= 1 and len(right) <= 1 and target not in left and target not in right:
                return False
