class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        
        if length == 1:
            return str(int(n) - 1)

        possible_palindromes = []
        
        left_half = n[:(length + 1) // 2]

        possible_palindromes.append(self.reflect(left_half, length % 2 == 0))
        possible_palindromes.append(self.reflect(str(int(left_half) + 1), length % 2 == 0))
        possible_palindromes.append(self.reflect(str(int(left_half) - 1), length % 2 == 0))

        possible_palindromes.append('9' * (length - 1))
        possible_palindromes.append('1' + '0' * (length - 1) + '1')

        closest = None
        min_diff = float('inf')
        original_num = int(n)

        for x in possible_palindromes:
            if x != n:
                candidate_num = int(x)
                diff = abs(candidate_num - original_num)

                if diff < min_diff or (diff == min_diff and candidate_num < int(closest)):
                    min_diff = diff
                    closest = x

        return closest

    def reflect(self, s: str, even_length: bool) -> str:
        if even_length:
            return s + s[::-1]
        else:
            return s + s[-2::-1]