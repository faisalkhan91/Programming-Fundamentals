"""
409. Longest Palindrome
https://leetcode.com/problems/longest-palindrome/?envType=study-plan&id=level-1

Palindrome:
A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards.
"""

# Second attempt to solve the problem:
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_map = dict.fromkeys(s, 0)
        for i in s:
            hash_map[i] += 1
        odds = 0
        for i in hash_map:
            if hash_map[i] % 2 != 0:
                odds += 1
        if odds > 0:
            odds -= 1
        return len(s) - odds

##############################################################################
# First attempt, but doesn't work.
# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         letters = dict.fromkeys(list(s), 0)
#         for i in (list(s)):
#             letters[i] += 1
#         count = 0
#         odd = 0
#         tripsie = 0
#         for i in letters:
#             if letters[i] % 2 == 0:
#                 count += letters[i]
#             elif letters[i] == 1:
#                 odd += 1
#             else:
#                 tripsie += 1
#                 count += letters[i]
#         if odd > 0 and tripsie == 0:
#             count += 1
#         return count
