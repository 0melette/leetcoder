from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(0, n):
            prefix[i] = prefix[i - 1] + nums[i]

        # spilting

        count = 0

        for i in range(0, n - 1):
            left = prefix[i]
            right = prefix[n - 1] - left
            if right <= left:
                count += 1

        return count

    # Time Complexity: O(n) - prefix sum calculation and then spilt checking
    # Space Complexity: O(n)
