"""
1657. Determine if Two Strings Are Close
https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75
"""

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        word1_freq = Counter(word1)
        word2_freq = Counter(word2)
        word1_set = list(word1_freq.values())
        word2_set = list(word2_freq.values())
        word1_set.sort()
        word2_set.sort()

        if word1_set == word2_set and set(word1) == set(word2):
            return True
        return False


word1 = "abc"
word2 = "bca"
execute = Solution()
print(execute.closeStrings(word1, word2))
