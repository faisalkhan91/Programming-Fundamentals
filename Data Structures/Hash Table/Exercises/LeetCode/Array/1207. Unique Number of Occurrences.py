"""
1207. Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/description/
"""
from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_map = Counter(arr)
        frequency_set = set(arr_map.values())

        return True if len(arr_map) == len(frequency_set) else False

    def uniqueOccurrences_oneliner(self, arr: List[int]) -> bool:
        return True if len(Counter(arr).values()) == len(set(Counter(arr).values())) else False


arr = [1,2,2,1,1,3]
execute = Solution()
print(execute.uniqueOccurrences(arr))
