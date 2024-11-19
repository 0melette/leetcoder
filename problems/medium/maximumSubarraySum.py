# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description

from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        current_sum = 0
        left = 0
        seen = set()

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            seen.add(nums[right])
            current_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1

        return max_sum
