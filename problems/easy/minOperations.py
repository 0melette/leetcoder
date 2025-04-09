from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k > min(nums):
            return -1
        nums_set = set(nums)
        unique_count = len(nums_set)
        if k in nums_set:
            return unique_count - 1
        else:
            return unique_count
