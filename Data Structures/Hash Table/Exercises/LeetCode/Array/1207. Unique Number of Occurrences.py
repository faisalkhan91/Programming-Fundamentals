"""
1207. Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/description/
"""

from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        In this solution a Hashmap and a Hashset are used to compare the number of occurrences. The Hashmap is used to
        count the occurrences of the values and the Hashset is used to check if the occurrences are unique. True is
        returned if the occurrences are unique, false otherwise.

        Time Complexity: O(n), Space Complexity: O(1).
        """
        arr_map = Counter(arr)  # Count the occurrences.
        frequency_set = set(arr_map.values())  # Check the uniqueness of the occurrences.
        return True if len(arr_map) == len(frequency_set) else False

    def uniqueOccurrences_oneliner(self, arr: List[int]) -> bool:
        """
        This is the one-liner of the above solution.
        """
        return True if len(Counter(arr).values()) == len(set(Counter(arr).values())) else False


arr = [1,2,2,1,1,3]
execute = Solution()
print(execute.uniqueOccurrences(arr))
