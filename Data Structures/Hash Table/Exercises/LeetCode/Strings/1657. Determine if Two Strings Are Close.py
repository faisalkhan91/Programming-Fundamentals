"""
1657. Determine if Two Strings Are Close
https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

Two strings are considered close if you can attain one from the other using the following operations:
    Operation 1: Swap any two existing characters.
        For example, abcde -> aecdb
    Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
        For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
"""

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        In this solution Hash Table is used to store the frequency of the letters in the word. The frequencies are
        compared along with the letters between the given words. If they match we return True else False.
        """

        word1_freq = Counter(word1)  # Word1 letter frequency.
        word2_freq = Counter(word2)  # Word2 letter frequency.
        word1_set = list(word1_freq.values())  # List of word1 frequencies.
        word2_set = list(word2_freq.values())  # List of word2 frequencies
        word1_set.sort()  # The list is sorted.
        word2_set.sort()

        # If the frequencies of the letters match and the letters also match, True is returned.
        if word1_set == word2_set and set(word1) == set(word2):
            return True
        return False

    def closeStrings(self, word1: str, word2: str) -> bool:
        return sorted(list(Counter(word1).values())) == sorted(list(Counter(word2).values())) and set(word1) == set(word2)


word1 = "abc"
word2 = "bca"
execute = Solution()
print(execute.closeStrings(word1, word2))
