class Solution:
    def getLucky(self, s: str, k: int) -> int:
        number = ""
        for x in s:
            number += str(ord(x) - ord('a') + 1)
        
        for _ in range(k):
            answer = 0
            for x in number:
                answer += int(x)
            number = str(answer)
        
        return int(number)