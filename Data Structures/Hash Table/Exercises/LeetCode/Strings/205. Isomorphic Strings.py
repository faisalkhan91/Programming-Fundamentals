"""
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1

** Isomorphic:
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
"""


class Solution:
    # Attempt to solve the isomorphic problem with one hash table. This can also be done with 2 hash maps as shown in
    # the solution for the problem on leetcode. Time complexity is O(n).
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = {}  # Create a hash map to store all the key value pairs.
        for i in range(len(s)):
            if s[i] not in dict_s.keys() and t[i] not in dict_s.values():
                dict_s[s[i]] = t[i]  # Add to the dictionary
        temp = ''
        for i in s:
            try:
                temp += str(dict_s[i])  # Create the word using values stored in the dictionary.
            except:
                pass
        print(t, temp)
        if t == temp:  # If the recreated values match then the strings are isomorphic.
            return True
        else:
            return False


s = "egg"
t = "add"
execute = Solution()
print(execute.isIsomorphic(s, t))
