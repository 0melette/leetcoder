from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.append(nums[num])
        return result

