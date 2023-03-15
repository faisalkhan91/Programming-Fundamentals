"""
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=study-plan&id=level-1
"""

from collections import Counter  # Used in solution 2.


class Solution:
    # Brute Force solution. This solution times out.
    def findAnagrams(self, s: str, p: str):

        s_substrings = {}
        for i in range(len(s) - len(p) + 1):
            s_substrings[i] = s[i:len(p) + i]
        anagram_index = []
        for i in s_substrings:
            if sorted(s_substrings[i]) == sorted(p):
                anagram_index.append(i)
        return anagram_index

    # Slightly optimized version of the above solution. Passes a lot more cases but still exceeds time limit.
    def findAnagrams_2(self, s: str, p: str):
        if len(s) == 0 or len(p) == 0:
            return
        if len(p) > len(s):
            return
        lenp = len(p)
        anagram_index = []
        p_hash = Counter(p)
        for i in range(len(s)):
            if Counter(s[i:lenp+i]) == p_hash:
                anagram_index.append(i)
        return anagram_index

    def findAnagrams_optimized(self, s: str, p: str):
        if len(p) > len(s):
            return
        letter_frequency_p = Counter(p)
        start_frequency_s = Counter(s[:len(p)])
        anagram_index = []

        if start_frequency_s == letter_frequency_p:
            anagram_index.append(0)

        for i in range(len(p), len(s)):
            if start_frequency_s[s[i - len(p)]] == 0:
                del start_frequency_s[s[i - len(p)]]
            else:
                start_frequency_s[s[i - len(p)]] -= 1
            start_frequency_s[s[i]] += 1
            if start_frequency_s == letter_frequency_p:
                anagram_index.append(i - len(p) + 1)
        return anagram_index


s = "cbaebabacd"
p = "abc"
execute = Solution()
print(execute.findAnagrams_optimized(s, p))

#########################################################################

# To check if the counter is same when there is a key with 0 as its value.
countertest1 = Counter('abe')
countertest2 = Counter('abc')
countertest2['c'] = 0
countertest2['e'] = 1
print(countertest1)
print(countertest2)

if countertest1 == countertest2:
    print('True')
else:
    print('False')
