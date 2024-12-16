from typing import List
   
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)

        for _ in range(k):
            min_index = 0
            for i in range(n):
                if nums[i] < nums[min_index]:
                    min_index = i

            nums[min_index] *= multiplier

        return nums
