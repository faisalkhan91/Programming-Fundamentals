"""
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/?envType=study-plan&id=level-1
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        This solution partially works but is complicated and does not account for lot of edge cases. This was using
        sliding window but work on a more favourable one was preferred.
        :param s:
        :param k:
        :return:
        """
        longest = 0
        max_string = 0
        s = list(s)
        for char in range(len(s) - 1):
            if s[char] == s[char + 1] and longest == 0:
                longest = 2
            elif s[char] == s[char + 1]:
                longest += 1
            elif s[char] != s[char + 1] and k > 0:
                s[char + 1] = s[char]
                if longest == 0:
                    longest = 2
                else:
                    longest += 1
                k -= 1
            else:
                longest = 0
            if longest > max_string:
                max_string = longest
        return max_string


    def characterReplacement2(self, s: str, k: int) -> int:
        """
        Reference: https://www.youtube.com/watch?v=gqXU1UyA8pk
        This is the implementation of the solution using sliding windows technique and a hash map. We use the left and
        right pointers to keep track of the sliding window. We keep incrementing the right pointer and calculating the
        frequency of the characters.

        The formula used to check for a valid substring would be:
        Length of the sliding window - Maximum frequency of the most frequent character <= k

        If the above condition fails we move the left pointer to the right to have a valid substring.

        :param s:
        :param k:
        :return: res
        """
        count = {}  # Create a hash map to store all the frequency of the letters.
        res = 0  # To store the result.

        left = 0  # Set the left pointer if the sliding window to 0.

        for right in range(len(s)):  # Increment the right pointer of the sliding window.
            count[s[right]] = 1 + count.get(s[right], 0)  # At each iteration update the frequency of the characters.

            # Increase the left pointer in the sliding window if the formula exceeds k. ((right-left)+1), there is + 1
            # because the starting indexes of left and right is 0 but the window size is 1.
            if ((right - left) + 1) - max(count.values()) > k:
                count[s[left]] -= 1  # Decrease the letter frequency of the character at left pointer.
                left += 1  # Move the left pointer to the right.

            # Store the max result between previous result and current sliding window.
            res = max(res, (right - left) + 1)

        return res

s = "AABABBA"
k = 1
execute = Solution()
print(execute.characterReplacement2(s, k))
