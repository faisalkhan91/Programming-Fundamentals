"""
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=study-plan&id=level-1
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        checker = list(p)
        anagram_index = []
        temp = []
        for i in range(len(s)):
            if s[i] in checker and len(checker) != 0:
                checker.pop(s[i])
                temp.append(i)
            elif len(checker) == 0:
                checker = list(p)
                anagram_index.append(temp[0])
                temp = []
        return anagram_index

    class Solution:
        def findAnagrams(self, s: str, p: str) -> List[int]:

            s_substrings = {}
            for i in range(len(s) - len(p) + 1):
                s_substrings[i] = s[i:len(p) + i]
            print(s_substrings)
            anagram_index = []
            for i in s_substrings:
                print(s_substrings[i])
                if hash(s_substrings[i]) == hash(p):
                    anagram_index.append(0)
            print(anagram_index)


