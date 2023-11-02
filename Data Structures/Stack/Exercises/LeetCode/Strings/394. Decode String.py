"""
394. Decode String
https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def decodeString(self, s: str) -> str:
        """
        In this solution, stack is used to store the substrings and the frequency of the sub strings. The current value
        of the frequency and also the current substring are stored in the stack (decoding) once a "[" is encountered.
        This is such that it decodes the inner brackets before the outer one. Once a "]" is encountered, the previous
        substring is popped from the stack as well as the previous frequency. The current substring is merged with the
        previous decoded substring retrieved from the stack.
        :param s:
        :return: decoded substring
        """

        decoding = []  # Stack to store the frequencies and previous substrings.
        curr_num = ''
        curr_str = ''

        for char in s:
            if char.isnumeric():
                curr_num += char  # Keep adding the char as the number can be 3 digits.
            elif char == '[':
                decoding.append(int(curr_num))  # If another "[", store the current frequency.
                decoding.append(curr_str)  # If another "[", store the current substring.
                curr_num = ''  # Reset the frequency.
                curr_str = ''  # Reset the substring.
            elif char == ']':
                prev_str = decoding.pop()  # Get the previous substring.
                prev_num = decoding.pop()  # Get the previous frequency.
                curr_str = prev_str + curr_str * prev_num  # Extend the current substring with the decoded substring.
            else:
                curr_str += char  # Add the characters to the current substring.

        return curr_str


s = "3[a2[c]]"
execute = Solution()
print(execute.decodeString(s))
