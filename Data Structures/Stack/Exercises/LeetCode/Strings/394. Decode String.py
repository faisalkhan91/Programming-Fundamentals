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
