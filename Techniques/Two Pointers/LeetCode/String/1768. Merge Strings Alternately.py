"""
1768. Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        In this solution we make use of two pointers technique to iterate through the string and add the letters to the
        merged string; then use slicing to add the remaining letters.

        Alternatively, the list pop method can be used.

        :param word1:
        :param word2:
        :return:
        """
        merged_word = ""
        word1_pointer = 0
        word2_pointer = 0

        while word1_pointer < len(word1) and word2_pointer < len(word2):
            merged_word = merged_word + word1[word1_pointer] + word2[word2_pointer]
            word1_pointer += 1
            word2_pointer += 1

        merged_word = merged_word + word1[word1_pointer:] + word2[word2_pointer:]

        return merged_word


word1 = "ab"
word2 = "pqrs"
execute = Solution()
print(execute.mergeAlternately(word1, word2))
