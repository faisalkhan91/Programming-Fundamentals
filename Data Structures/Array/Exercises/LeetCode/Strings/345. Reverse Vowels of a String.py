"""
345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        This solution makes use of two pointer technique. Two pointers, left and right, are used to search for vowels
        and swap them if found.
        :param s:
        :return: Reversed vowel string.
        """

        left = 0  # Start from the left of the string.
        right = len(s) - 1  # Start from the right of the string.
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  # Make a list of all the vowels.
        s = list(s)  # Convert the string to a list.

        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1  # After swapping move to the next letters in the string.
                right -= 1

        return ''.join(s)  # Return a joined string.


s = "hello"
execute = Solution()
print(execute.reverseVowels(s))
