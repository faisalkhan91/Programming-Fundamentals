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




#----------------------------------------------------------------#

    def characterReplacement(self, s: str, k: int) -> int:

        substring_frequency = {}
        count = 1
        max = 0
        max_dict = {}

        for index in range(len(s) - 1):
            # if s[index] in substring_frequency and s[index] == s[index - 1]:
            #     substring_frequency[s[index]][s[index]] += 1
            # else:
            #     substring_frequency[s[index]] = {s[index] + str(index): 1}

            print(index, len(s))
            if s[index] == s[index + 1]:
                count += 1
            else:
                if s[index] not in substring_frequency:
                    substring_frequency[s[index]] = {}
                    substring_frequency[s[index]].update({s[index] + str(index): count})
                else:
                    substring_frequency[s[index]].update({s[index] + str(index): count})
                count = 1
                if index + 1 == len(s) - 1:
                    substring_frequency[s[index + 1]].update({s[index + 1] + str(index): count})
            if count > max:
                max = count
                max_dict.update()

        print(substring_frequency)

        return 0