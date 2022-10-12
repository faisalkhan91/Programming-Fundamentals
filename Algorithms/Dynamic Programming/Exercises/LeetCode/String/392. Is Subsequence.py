"""
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/?envType=study-plan&id=level-1

Subsequence:
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
"abcde" while "aec" is not).
"""


class Solution:
    # Time complexity is O(n). This is a two pointer method to solve the problem, not dynamic programming. The dynamic
    # programming solution is referenced here:
    # https://stackoverflow.com/questions/74035067/python-solution-for-392-is-subsequence/74036291#74036291
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        temp = ''
        count = 0
        for i in t:
            if count < len(s) and i == s[count]:
                temp += i
                count += 1
        if temp == s:
            return True
        else:
            return False


s = "b"
t = "abc"
execute = Solution()
print(execute.isSubsequence(s, t))
