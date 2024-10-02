from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        rank_map = {num: rank for rank, num in enumerate(sorted_unique, start=1)}
        return [rank_map[num] for num in arr]
