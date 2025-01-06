from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        difference = n * [0]

        for shift in shifts:
            value = 1 if shift[2] == 1 else -1 if shift[2] == 0 else 0
            for i in range(shift[0],shift[1]+1):
                difference[i] += value
        
        # applying shift
        
        result = list(s)

        for i in range(n):
            shifted_char = chr((ord(s[i]) - ord("a") + difference[i]) % 26 + ord("a"))
            result[i] = shifted_char

        return "".join(result);

                
