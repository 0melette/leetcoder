from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        
        result = []
        for i in range(m):
            row = original[i * n: (i + 1) * n]
            result.append(row)
        
        return result