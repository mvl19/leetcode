from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            if target not in nums:
                return -1
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if target not in nums:
                return -1
            if target == nums[l]:
                return l
            if target == nums[r]:
                return r
            if target in nums[l:m]:
                r = m
            if target in nums[m:r]:
                l = m
