from typing import List

class Solution:
    def possibleStringCount(self, word: str) -> int:
        result = 1
        prev = None
        for c in word:
            if c == prev:
                result += 1
            else:
                prev = c
        return result