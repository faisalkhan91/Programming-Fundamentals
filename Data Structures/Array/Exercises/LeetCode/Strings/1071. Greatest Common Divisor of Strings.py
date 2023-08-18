"""
1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75
"""
from collections import Counter


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        pass


#############################################################################

# Initial attempt, unfortunately the log is not correct for the below implementation as the string does not divide
# properly for the example str1 = "LEET" and str2 = "Code".
#
# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#
#         GCD = 0
#
#         str1_frequency = Counter(str1)
#         str2_frequency = Counter(str2)
#
#         if len(str1) > len(str2) or len(str1) < len(str2):
#             long_string = max(str1_frequency, str2_frequency)
#             short_string = min(str1_frequency, str2_frequency)
#         else:
#             long_string = str1_frequency
#             short_string = str2_frequency
#
#         for i in long_string:
#             print(i, short_string.keys())
#             if i in short_string.keys():
#                 print("hey")
#                 GCD += 1
#                 print(min(long_string[i], short_string[i]))
#
#         return str1[:GCD]
