from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        n = len(words)

        prefix = [0] * (n + 1)

        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prefix[i + 1] = prefix[i] + 1  # add
            else:
                prefix[i + 1] = prefix[i]

        # retrieving for query

        result = []
        for l, r in queries:
            count = prefix[r + 1] - prefix[l]
            result.append(count)

        return result
