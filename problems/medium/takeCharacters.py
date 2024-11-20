class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        total_a = total_b = total_c = 0
        for char in s:
            if char == 'a':
                total_a += 1
            elif char == 'b':
                total_b += 1
            elif char == 'c':
                total_c += 1
        if total_a < k or total_b < k or total_c < k:
            return -1

        required_a = k
        required_b = k
        required_c = k

        max_window_size = 0
        window_a = window_b = window_c = 0
        start = 0

        for end in range(n):
            if s[end] == 'a':
                window_a += 1
            elif s[end] == 'b':
                window_b += 1
            elif s[end] == 'c':
                window_c += 1

            while total_a - window_a < required_a or total_b - window_b < required_b or total_c - window_c < required_c:
                if s[start] == 'a':
                    window_a -= 1
                elif s[start] == 'b':
                    window_b -= 1
                elif s[start] == 'c':
                    window_c -= 1
                start += 1

            max_window_size = max(max_window_size, end - start + 1)

        return n - max_window_size

