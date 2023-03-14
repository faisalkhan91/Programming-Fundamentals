"""
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=study-plan&id=level-1
"""


class Solution:
    def findAnagrams(self, s: str, p: str):

        s_substrings = {}
        for i in range(len(s) - len(p) + 1):
            s_substrings[i] = s[i:len(p) + i]
        anagram_index = []
        for i in s_substrings:
            if sorted(s_substrings[i]) == sorted(p):
                anagram_index.append(i)
        return anagram_index


s = "cbaebabacd"
p = "abc"
execute = Solution()
print(execute.findAnagrams(s, p))
