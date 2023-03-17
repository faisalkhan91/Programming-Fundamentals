"""
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/?envType=study-plan&id=level-1
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start_index = 0
        end_index = 0
        for i range(len(s)):
             start_index = i
             if flag