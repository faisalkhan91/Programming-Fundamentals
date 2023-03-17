"""
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/?envType=study-plan&id=level-1
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        max_string = 0
        for char in range(len(s) - 1):
            if s[char] == s[char + 1] and longest == 0:
                longest += 2
            elif s[char] == s[char + 1]:
                longest += 1
            elif s[char] != s[char + 1] and k > 0:
                s.replace(s[char], s[char + 1])
                longest += 1
                k -= 1
            else:
                longest = 1
            if longest > max_string:
                max_string = longest
        return max_string