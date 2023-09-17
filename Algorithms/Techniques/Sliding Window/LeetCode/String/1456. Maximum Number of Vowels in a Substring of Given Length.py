"""
1456. Maximum Number of Vowels in a Substring of Given Length
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        In this solution the sliding window technique is used to traverse the string. The initial count of the vowels is
        calculated by the given window size and then a while loop is used to move the window to the right, each letter
        entering the string is checked for the vowel parameters, if it is a vowel the current_vowel count is incremented
        by 1, similarly if the letter leaving the window is a vowel the current count is decremented. Each iteration is
        compared with the previous max count and stored accordingly.
        :param s:
        :param k:
        :return: max_vowels
        """
        left = 0
        right = k
        vowels = ['a', 'e', 'i', 'o', 'u']
        max_vowels = 0

        # Calculate the count of the initial window.
        for i in range(k):
            if s[i] in vowels:
                max_vowels += 1

        current_vowels = max_vowels  # Set the current count as the previous max count.
        while right < len(s):
            if s[right] in vowels:
                current_vowels += 1
            if s[left] in vowels:
                current_vowels -= 1
            max_vowels = max(max_vowels, current_vowels)  # Compare current count in each iteration.
            right += 1
            left += 1

        return max_vowels


s = "abciiidef"
k = 3
execute = Solution()
print(execute.maxVowels(s, k))
