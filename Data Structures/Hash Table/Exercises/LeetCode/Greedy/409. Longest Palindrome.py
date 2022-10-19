"""
409. Longest Palindrome
https://leetcode.com/problems/longest-palindrome/?envType=study-plan&id=level-1

Palindrome:
A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards.
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        This is my attempt to solve the problem without checking the discuss section on leetcode.
        :param s:
        :return:
        """
        hash_map = dict.fromkeys(s, 0)  # Initialize a hash table using dictionary and set all the letter frequencies 0.
        for i in s:  # Count the occurrences of the letters in the string.
            hash_map[i] += 1
        odds = 0  # Variable to count the number of odd occurrences of letters.
        for i in hash_map:
            if hash_map[i] % 2 != 0:  # If the letter frequency is odd in the string.
                odds += 1  # Increment the odd counter.
        # If there are odd letter frequencies in the string subtract 1 from odd counter as we can form a palindrome with
        # one odd occurrence.
        if odds > 0:
            odds -= 1
        return len(s) - odds

    def longestPalindrome_optimized(self, s: str) -> int:
        """
        This is one of the optimized solutions from leetcode. Here we add letters to set if the letters are not in set
        and remove the letters if they are in the set. If at the end of the loop there are any letters left in the set,
        they are the odd occurences of the letters and can be subtracted from the length of the string to find the
        longest palindrome.
        :param s:
        :return:
        """
        check_set = set()  # Set to check the odd occurrences.
        odd = 0  # Flag to check if there were any odd occurrences in the string.
        for i in s:
            if i not in check_set:
                check_set.add(i)
            else:
                check_set.remove(i)
        if len(check_set) > 0:
            odd = 1
        return len(s) - len(check_set) + odd


s = "abccccdd"
execute = Solution()
print(execute.longestPalindrome(s))

##############################################################################
# First attempt, but doesn't work.
# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         letters = dict.fromkeys(list(s), 0)
#         for i in (list(s)):
#             letters[i] += 1
#         count = 0
#         odd = 0
#         tripsie = 0
#         for i in letters:
#             if letters[i] % 2 == 0:
#                 count += letters[i]
#             elif letters[i] == 1:
#                 odd += 1
#             else:
#                 tripsie += 1
#                 count += letters[i]
#         if odd > 0 and tripsie == 0:
#             count += 1
#         return count
