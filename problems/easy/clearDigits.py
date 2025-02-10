class Solution:
    def clearDigits(self, s: str) -> str:
        result = ""
        for c in s:
            if c.isdigit():
                if result:
                    result = result[:-1]
            else:
                result += c
        return result
