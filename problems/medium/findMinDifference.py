from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            total_minutes = h * 60 + m
            minutes.append(total_minutes)
        minutes.sort()

        min_diff = 1440 
        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i - 1]
            min_diff = min(min_diff, diff)
            if min_diff == 0:
                return 0 
            
        circular_diff = (minutes[0] + 1440) - minutes[-1]
        min_diff = min(min_diff, circular_diff)
        
        return min_diff