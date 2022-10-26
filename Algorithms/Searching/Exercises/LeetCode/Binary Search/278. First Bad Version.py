"""
278. First Bad Version
https://leetcode.com/problems/first-bad-version/
"""


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        start = 1  # Set the start as the first version.
        end = n  # Set end as the last version.
        bad = 0  # Variable to store the first occurrence of bad version.

        if isBadVersion(start) is True:  # If the first version is bad return the first version.
            return start

        while start <= end:  # As long as start and end don't overlap, keep looping.
            mid = (start + end) // 2  # Since we are doing a binary search method we find the middle version.
            if isBadVersion(mid) is True:  # If we find the bad version, we move to left to see if this is the first.
                end = mid - 1  # Set end to the left of the middle element in the current list.
                bad = mid  # Store the bad version.
            else:
                start = mid + 1  # Set start to the right if the middle element is false as we discard the left side.

        return bad
