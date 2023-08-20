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

# This solution passes the initial test cases but fails to recognize the dividable factor. For example, it fails at the
# test inputs of str1 = "ABCDEF", str2 = "ABC".
#
# def gcdOfStrings(self, str1: str, str2: str) -> str:
#
#     GCD = 0
#     char_list = {}
#     i = 0
#     j = 0
#
#     while len(str1) - i > 0 and len(str2) - i > 0:
#         if str1[i] in char_list:
#             char_list[str1[i]] = char_list[str1[i]] + 1
#         else:
#             char_list[str1[i]] = 1
#         if str1[i] == str2[i] and char_list[str1[i]] % 2 != 0:
#             GCD += 1
#         i += 1
#
#     return str1[:GCD]

# This soluition only works partially and fails for test cases such as,
# str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX", str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
#
# def gcdOfStrings(self, str1: str, str2: str) -> str:
#     str1_freq = Counter(str1)
#     str2_freq = Counter(str2)
#
#     if str1 + str2 != str2 + str1:
#         return ""
#
#     GCD = 0
#
#     for i in str1_freq:
#         if str1_freq[i] == 1 or str2_freq[i] == 1:
#             GCD += 1
#         elif str1_freq[i] > str2_freq[i]:
#             GCD = GCD + (str1_freq[i] // str2_freq[i])
#         else:
#             GCD = GCD + (str2_freq[i] // str1_freq[i])
#
#     # if (max(len(str1), len(str2)) % GCD) != 0:
#     #     GCD = GCD + (max(len(str1), len(str2)) % GCD)
#
#     return str1[:GCD]
