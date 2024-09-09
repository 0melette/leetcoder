from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        remaining_list = [0] * n
        total = mean * (len(rolls) + n)
        current_total = sum(rolls)
        remaining = total - current_total
        if remaining < n or remaining > 6 * n:
            return []  
        whole = remaining // n
        left = remaining % n
        for i in range(n): 
            remaining_list[i] = whole + (1 if i < left else 0)
        return remaining_list