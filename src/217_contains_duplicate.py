from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prevMap = set()
        for val in nums:
            if val in prevMap:
                return True
            prevMap.add(val)
        return False
