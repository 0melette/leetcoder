from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
            nums = list(map(str, nums))
            nums.sort(key=lambda x: x*10, reverse=True)
            
            if nums[0] == '0':
                return '0'
            
            return ''.join(nums)
