from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for index, val in enumerate(nums):
            diff = target - val
            if diff in prev:
                return [prev[diff], index]
            prev[val] = index