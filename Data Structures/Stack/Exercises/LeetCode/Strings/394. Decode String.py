"""
394. Decode String
https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def decodeString(self, s: str) -> str:
        decoded = ''
        coding = 0
        substring = ''

        for i in range(len(s)):
            if s[i].isalpha():
                substring += s[i]
            if s[i].isnumeric():
                coding = int(s[i])
            if s[i] == ']':
                for j in range(coding):
                    decoded += substring
                substring = ''

        return decoded


    def decodeString(self, s: str) -> str:
        frequencies = []
        decoded = []
        sub_str = ''
        for char in s:
            if char == "]":
                num = int(frequencies.pop())
                decoded.append(sub_str * num)
                sub_str = ''
            elif char == "[":
                decoded.append(sub_str)
                sub_str = ''
            elif char.isalpha():
                sub_str += char
            elif char.isnumeric():
                frequencies.append(char)
            print(decoded)
        return ''.join(decoded)