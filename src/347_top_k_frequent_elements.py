from typing import List
from collections import Counter


class Solution:
    def productExceptSelf(self, nums: List[int], k) -> List[int]:
        counter = Counter(nums)
        return [n for n, _ in counter.most_common(k)]

