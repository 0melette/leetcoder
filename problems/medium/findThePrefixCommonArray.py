from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen_a = set()
        seen_b = set()
        common_count = 0
        result = []

        for i in range(n):
            if A[i] not in seen_a:
                seen_a.add(A[i])
                if A[i] in seen_b:
                    common_count += 1
            if B[i] not in seen_b:
                seen_b.add(B[i])
                if B[i] in seen_a:
                    common_count += 1

            result.append(common_count)

        return result
