"""
1456. Maximum Number of Vowels in a Substring of Given Length
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        right = k
        vowels = ['a', 'e', 'i', 'o', 'u']
        current_vowels = max_vowels = 0

        for i in range(k):
            if s[i] in vowels:
                max_vowels += 1

        current_vowels = max_vowels
        while right < len(s):
            if s[right] in vowels:
                current_vowels += 1
            if s[left] in vowels:
                current_vowels -= 1
            max_vowels = max(max_vowels, current_vowels)
            right += 1
            left += 1

        return max_vowels


s = "abciiidef"
k = 3
execute = Solution()
print(execute.maxVowels(s, k))
