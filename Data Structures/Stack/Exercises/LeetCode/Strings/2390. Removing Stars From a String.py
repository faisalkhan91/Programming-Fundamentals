"""
2390. Removing Stars From a String
https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)
        i = len(s) - 1

        while i > 0:
            if s[i] == '*':
                s.pop()
                s.pop()
                i -= 2
            else:
                i -= 1

        print(s)
