"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/description/?envType=study-plan&id=level-1
"""

class Solution:
    # Brute force approach.
    def uniquePaths(self, m: int, n: int) -> int:
        completed_paths = [0]
        def routes(i, j):
            if i == m - 1 and j == n - 1:
                completed_paths[0] += 1
                return
            if i > m - 1 or j > n - 1:
                return
            routes(i + 1, j)
            routes(i, j + 1)
        routes(0, 0)
        return completed_paths[0]

    def uniquePaths_bruteforce_2(self, m: int, n: int) -> int:
        completed_paths = [0]
        grid = [[0 for i in range(n)] for j in range(m)]
        grid[m - 1][n - 1] = 1
        def routes(i, j):
            if i > m - 1 or j > n - 1:
                return
            if grid[i][j] == 1:
                completed_paths[0] += 1
                return
            routes(i + 1, j)
            routes(i, j + 1)
        routes(0, 0)
        return completed_paths[0]


m = 2
n = 3
execute = Solution()
execute.uniquePaths(m, n)



######## Not working solutions #########
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

    #############################

    class Solution:
        def uniquePaths(self, m: int, n: int) -> int:
            completed_paths = [0]
            check = []

            def routes(i, j):
                print(i, j)
                print(check)

                if i == m - 1 and j == n - 1:
                    completed_paths[0] += 1
                    return
                if i > m - 1 or j > n - 1:
                    return
                if (i, j) not in check:
                    check.append((i, j))
                    routes(i + 1, j)
                    routes(i, j + 1)
                else:
                    return

            routes(0, 0)
            print(len(check))
            return completed_paths[0]
