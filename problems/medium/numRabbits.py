from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = {}
        amount = 0
        for a in answers:
            if a in freq:
                freq[a] += 1
            else:
                freq[a] = 1

        for n in freq:
            if n == 0:
                amount += freq[n]
            else:
                max_size = n + 1
                full_groups = freq[n] // max_size
                remainder = freq[n] % max_size

                if remainder > 0:
                    groups = full_groups + 1
                else:
                    groups = full_groups

                amount += groups * max_size

        return amount

