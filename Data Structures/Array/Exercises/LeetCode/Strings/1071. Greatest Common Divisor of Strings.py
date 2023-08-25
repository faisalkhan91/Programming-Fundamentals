"""
1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75
"""
from collections import Counter


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        In this solution the string is checked if it s divisible by calculating the factor.
        :param str1:
        :param str2:
        :return: str[i], ""
        """

        len1, len2 = len(str1), len(str2)  # Pre-calculate the length of the strings.

        # Create helper function, to find the divisor of the string.
        def is_divisor(l):
            # Check if the string is divisible by yhe current length but taking modulus and seeing if the mod return 0.
            # For example if len % l == 0, then the string is divisible and it WON'T return false.
            if len1 % l or len2 % l:
                return False
            f1, f2 = len1 // l, len2 // l  # Calculate the factor of each string.
            # Multiply str1 with the factor and see if it produces str1 and str2 and return True.
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for i in range(min(len1, len2), 0, -1): # We start with the reverse of the smallest string.
            if is_divisor(i):
                return str1[:i]

        return ""  # Return default if no divisible string found.


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
# str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX", str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX", as it doesn't account for
# duplicate letters like above 'XX'.
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

# Another one that fails for another test case.
#
# def gcdOfStrings(self, str1: str, str2: str) -> str:
#
#     if str1 + str2 != str2 + str1:
#         return ""
#
#     str1_freq = Counter(str1)
#     str2_freq = Counter(str2)
#     GCD = 0
#
#     for i in str1_freq:
#         if str1_freq[i] == 1 or str2_freq[i] == 1:
#             GCD += 1
#         else:
#             GCD = GCD + min(str1_freq[i] // len(str1_freq), str2_freq[i] // len(str2_freq))
#
#     return str1[:GCD]
