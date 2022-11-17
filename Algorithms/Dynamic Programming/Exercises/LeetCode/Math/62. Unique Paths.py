"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/description/?envType=study-plan&id=level-1
"""


################### Still working, trying alternative solution.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        store_paths = [0]

        def paths(m, n):

            if m == 0 and n == 0:
                store_paths[0] += 1
            if m < 0 or n < 0:
                return
            paths(m - 1, n)
            paths(m, n - 1)

            return store_paths

        return paths(m, n)


    ##############################
    paths = 0
    path_1 = 1
    path_2 = 2

    for i in range(m):
        for j in range(n):
            