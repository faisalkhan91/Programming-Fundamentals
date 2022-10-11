"""
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1

** Isomorphic:
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = {}
        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = t[i]
        temp = ''
        for i in t:
            temp += str(list(dict_s.values()).index(i))

        print(temp)

        return False


s = ''
t = ''
execute = Solution()
print(execute.isIsomorphic(s, t))