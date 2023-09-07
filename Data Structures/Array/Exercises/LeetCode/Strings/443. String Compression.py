"""
443. String Compression
https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def compress(self, chars) -> int:
        """
        In this solution, an empty string is initialized to store the character and character count (if > 1). Two
        pointers are used to iterate through the string and compare the current character to the next character. Once
        the next character is hit, the current character and the difference of the pointer positions is added to the
        string. Then we iterate through the string to add the compression information to the char array and return the
        len of the s array.
        :param chars:
        :return: Length of chars array where the compression information is stored.
        """
        s = ""  # Empty string
        current_char = 0  # First pointer
        next_char = 1  # Second pointer

        while next_char < len(chars):  # While there is still a character left to compare.
            if chars[current_char] != chars[next_char]:  # Once we encounter a new character
                s = s + chars[current_char]
                if next_char - current_char > 1:  # Don't add the count if it is less than 1.
                    s = s + str(next_char - current_char)
                current_char = next_char
            next_char += 1

        # Add the last character info, since our while loops ends before doing that.
        s = s + chars[current_char]
        if next_char - current_char > 1:
            s = s + str(next_char - current_char)

        # Add the compression information to the character array.
        for i in range(len(s)):
            chars.insert(i, s[i])

        return len(s)


chars = ["a","a","b","b","c","c","c"]
execute = Solution()
print(chars[:execute.compress(chars)])
