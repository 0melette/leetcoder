from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        if k == 0:
            return [0] * n # if k is 0, all numbers become 0
        
        result = [0] * n
        extended_list = code * 2

        if k > 0:
            window_sum = sum(extended_list[1:1 + k])
            for i in range(n):
                result[i] = window_sum
                window_sum += extended_list[i + k + 1] - extended_list[i + 1]

        if k < 0:
            k = -k
            window_sum = sum(extended_list[n - k:n])
            for i in range(n):
                result[i] = window_sum
                window_sum += extended_list[i + n] - extended_list[i + n - k]

        return result