"""
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        In this solution we use split to split the words based on the spaces between words and then concatenate the
        string back in reversed order skipping the extra spaces.
        :param s:
        :return: reversed_s
        """
        s = s.split(" ")
        reversed_string = ''

        for word in reversed(s):
            if word != '':
                reversed_string = reversed_string + word + ' '

        return reversed_string[:-1]


s = "the sky is blue"
execute = Solution()
print(execute.reverseWords(s))
