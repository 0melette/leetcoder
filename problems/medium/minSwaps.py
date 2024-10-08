class Solution:
    def minSwaps(self, s: str) -> int:
        stack_size = 0
        for char in s:
            if char == '[':
                stack_size += 1
            else:
                if stack_size > 0:
                    stack_size -= 1
        return (stack_size + 1) // 2
