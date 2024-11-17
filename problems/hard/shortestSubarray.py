# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        dq = deque()
        dq.append(0) 
        result = n + 1 
        
        for i in range(1, n + 1):
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                result = min(result, i - dq[0])
                dq.popleft()
            
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        if result <= n:
            return result
        else:
            return -1

# Beats 83%
# Time Complexity: O(n)
# Space Complexity: O(n)
# Prefix Sum + Monotonic Dequeue