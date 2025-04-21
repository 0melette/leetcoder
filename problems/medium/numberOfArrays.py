from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for num in differences:
            prefix.append(prefix[-1] + num)

        print(prefix)
        prefix_range = max(prefix) - min(prefix) + 1
        print(prefix_range)
        num_range = upper - lower + 1
        print(num_range)

        return max(0, num_range - prefix_range + 1)

