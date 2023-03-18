"""
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/?envType=study-plan&id=level-1
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        This solution partially works but is complicated and does not account for lot of edge cases. This was using
        sliding window but work on a more favourable one was preferred.
        :param s:
        :param k:
        :return:
        """
        longest = 0
        max_string = 0
        s = list(s)
        for char in range(len(s) - 1):
            if s[char] == s[char + 1] and longest == 0:
                longest = 2
            elif s[char] == s[char + 1]:
                longest += 1
            elif s[char] != s[char + 1] and k > 0:
                s[char + 1] = s[char]
                if longest == 0:
                    longest = 2
                else:
                    longest += 1
                k -= 1
            else:
                longest = 0
            if longest > max_string:
                max_string = longest
        return max_string