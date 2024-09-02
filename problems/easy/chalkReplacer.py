from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        round = sum(chalk)
        k %= round
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]