from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # track maximum number of decrements for each index by RATE OF CHANGE
        tracker = [0 for _ in nums]
        for l, r in queries:
            tracker[l] += 1
            # case when r is on the right boundary
            if r + 1 < len(tracker):
                tracker[r + 1] -= 1
        cur = 0
        for i, v in enumerate(tracker):
            cur += v
            if cur >= nums[i]:
                continue
            else:
                return False
        return True

