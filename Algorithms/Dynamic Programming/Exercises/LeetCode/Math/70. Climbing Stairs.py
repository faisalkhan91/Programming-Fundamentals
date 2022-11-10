"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/description/
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        ways_to_climb = set()
        steps = []
        m = 0

        def routes(n, m):
            if m > n:
                ways_to_climb.add(tuple(steps))
                return ways_to_climb

            steps.append(m)
            routes(n, m + 1)
            routes(n, m + 2)

        routes(n, m)
        return len(ways_to_climb)


n = 25
execute = Solution()
print(execute.climbStairs(n))
