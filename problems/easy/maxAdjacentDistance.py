from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        count = len(nums)
        biggest_diff = abs(nums[count - 1] - nums[0])

        for i in range(len(nums) - 1):
            current_diff = abs(nums[i + 1] - nums[i])
            if current_diff > biggest_diff:
                biggest_diff = current_diff
        return biggest_diff

