"""
2390. Removing Stars From a String
https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def removeStars(self, s: str) -> str:
        """
        In this solution, stack is used to store the characters from the string and pop the last character when a * is
        encountered.
        """

        non_star = []  # The List is declared as stack. This will hold the resulting string.
        for char in s:
            if char == '*':
                non_star.pop()  # Pop the last character when a * is encountered.
            else:
                non_star.append(char)  # Keep adding the characters to the stack.

        return ''.join(non_star)


s = "leet**cod*e"
execute = Solution()
print(execute.removeStars(s))
