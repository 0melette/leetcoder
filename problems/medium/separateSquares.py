from typing import List
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def area_below(mid: float) -> float:
            area = 0.0
            for square in squares:
                x, y, l = square
                if y >= mid:
                    continue
                elif y + l <= mid:
                    area += l * l
                else:
                    height = mid - y
                    area += l * height
            return area

        # x y l 
        # total area calculations
        total_area = sum(square[2] * square[2] for square in squares)
        mid_area = total_area / 2

        low = min(square[1] for square in squares)  # we need to check all squares for min y O(n)
        high = max(square[1] + square[2] for square in squares) # the max height is the max(y + l) of all squares

        # binary search for mid 
        for _ in range(67): 
            mid = (low + high) / 2
            if area_below(mid) < mid_area:
                low = mid
            else:
                high = mid
        return float(f"{low:.5f}")

# https://leetcode.com/problems/separate-squares-i/description/