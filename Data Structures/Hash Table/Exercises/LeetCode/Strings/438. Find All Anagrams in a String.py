"""
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=study-plan&id=level-1
"""

from collections import Counter  # Used in solution 2 and 3.


class Solution:
    def findAnagrams(self, s: str, p: str):
        """
        Brute Force solution. This solution times out on test cases in LeetCode. In this solution a hash map of all the
        possible substrings that are the size of string p is made. Then the hash map is iterated through and compared
        with the p string to see if it matches. Time complexity is O(m+n). Space complexity is O(m).
        :param s:
        :param p:
        :return:
        """
        s_substrings = {}
        for i in range(len(s) - len(p) + 1):  # Create a hash map.
            s_substrings[i] = s[i:len(p) + i]
        anagram_index = []
        for i in s_substrings:
            if sorted(s_substrings[i]) == sorted(p):  # Sort the string to compare.
                anagram_index.append(i)
        return anagram_index

    def findAnagrams_2(self, s: str, p: str):
        """
        Slightly optimized version of the above solution. Passes a lot more cases but still exceeds time limit. Uses
        Counter to compare the letter frequency of each substring with p. The window recounts the frequency of each
        substring individually.
        :param s:
        :param p:
        :return:
        """
        if len(s) == 0 or len(p) == 0:
            return
        if len(p) > len(s):
            return
        lenp = len(p)
        anagram_index = []
        p_hash = Counter(p)
        for i in range(len(s)):
            if Counter(s[i:lenp+i]) == p_hash:  # Calculate and compare the letter frequencies.
                anagram_index.append(i)
        return anagram_index

    def findAnagrams_optimized(self, s: str, p: str):
        """
        In this solution the letter frequency of the first substring is calculated and sliding window of size p
        traverses the string s. Instead of calculating the frequency of each substring, only the frequency of the new
        character entering the window is updated in the starting frequency of the original substring while the character
        that is leaving the window is subtracted by 1. This makes the solution more efficient by not calculating the
        frequency of each substring.
        :param s:
        :param p:
        :return:
        """
        if len(p) > len(s):
            return
        letter_frequency_p = Counter(p)  # Letter frequency of p.
        start_frequency_s = Counter(s[:len(p)])  # Starting substring frequency.
        anagram_index = []

        if start_frequency_s == letter_frequency_p:  # If the first substring is an anagram.
            anagram_index.append(0)

        for i in range(len(p), len(s)):
            start_frequency_s[s[i - len(p)]] -= 1  # Subtract the character leaving the window.
            start_frequency_s[s[i]] += 1  # Add the character entering the window.
            if start_frequency_s == letter_frequency_p:
                # Here subtract the length of the p string and add 1 as we are keeping track of the new character, we
                # have to find the starting index of the matched substring.
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
