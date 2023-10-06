"""
1657. Determine if Two Strings Are Close
https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_set = set(word1)
        word2_set = set(word2)

        if word1_set == word2_set and len(word1) == len(word2):
            return True
        return False


word1 = "abc"
word2 = "bca"
execute = Solution()
print(execute.closeStrings(word1, word2))
