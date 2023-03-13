"""
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=study-plan&id=level-1
"""

from string import ascii_lowercase as abc


class Solution:
    def findAnagrams(self, s: str, p: str):

        s_substrings = {}
        for i in range(len(s) - len(p) + 1):
            s_substrings[i] = s[i:len(p) + i]
        anagram_index = []
        for i in s_substrings:
            print(s_substrings[i], p)
            for c in abc[:-1]:
                if s_substrings[i].count(c) != p.count(c):
                    break
                anagram_index.append(i)
                break
        return anagram_index


s = "bae"
p = "abc"
execute = Solution()
print(execute.findAnagrams(s, p))
