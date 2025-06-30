from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        max_sum = 0
        map = Counter(nums)
        for key in map:
            # print(f"key: {key}, value: {map[key]}")
            if key + 1 in map:
                total = map[key] + map[key + 1]
                max_sum = max(max_sum, total)
        # print(map)
        return max_sum

