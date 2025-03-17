from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        freq = {}
    
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        for count in freq.values():
            if count % 2 != 0:
                return False
        return True

