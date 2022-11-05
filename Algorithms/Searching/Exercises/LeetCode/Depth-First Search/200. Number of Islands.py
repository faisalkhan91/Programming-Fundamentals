"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num_of_islands = 0
        for row in range(m):
            for column in range(n):
                if grid[row][column] == "1":
                    num_of_islands += 1
                    self.visit_island(grid, row, column)

        return num_of_islands

    def visit_island(self, grid, row, column):
        m = len(grid)
        n = len(grid[0])
        if row < 0 or row > m - 1 or column < 0 or column > n - 1:
            return
        if grid[row][column] == "0":
            return
        if grid[row][column] == "2":
            return
        if grid[row][column] == "1":
            grid[row][column] = "2"
        print("row", row, "column", column)
        self.visit_island(grid, row + 1, column)
        self.visit_island(grid, row - 1, column)
        self.visit_island(grid, row, column + 1)
        self.visit_island(grid, row, column - 1)

        return grid
