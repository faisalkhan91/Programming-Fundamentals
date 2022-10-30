"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return self.islands(grid, 0, 0, 0, grid[0][0])

    def islands(self, grid, row, column, count, prev):
        m = len(grid)
        n = len(grid[0])
        if row < 0 or row > m - 1 or column < 0 or column > n - 1:
            return
        if grid[row][column] == "0":
            return
        if grid[row][column] == prev:
            count += 1
        print("row", row, "column", column)
        self.islands(grid, row + 1, column, count, prev)
        self.islands(grid, row - 1, column, count, prev)
        self.islands(grid, row, column + 1, count, prev)
        self.islands(grid, row, column - 1, count, prev)
