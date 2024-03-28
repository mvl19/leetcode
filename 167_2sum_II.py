from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0
        while r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] < target:
                l += 1
