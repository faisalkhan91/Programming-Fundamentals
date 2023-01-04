"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/description/?envType=study-plan&id=level-1
"""


class Solution:
    # Brute force approach. This fails once the grid becomes large enough. In this approach a nested method is used to
    # calculate the routes and store the completed routes whenever the i and j indexes reach the m - 1 and n - 1 index.
    def uniquePaths(self, m: int, n: int) -> int:
        completed_paths = [0]  # Stores

        def routes(i, j):
            if i == m - 1 and j == n - 1:  # If i and j are in the bottom right corner of the grid.
                completed_paths[0] += 1  # Add to the path to the completed path.
                return
            if i > m - 1 or j > n - 1:  # If i or j exceeded the grid length stop processing.
                return
            routes(i + 1, j)  # Call the method to move down.
            routes(i, j + 1)  # Call the method to move up.
        routes(0, 0)  # Start with the 0 index.
        return completed_paths[0]

    # Brute force alternative approach.
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
