"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Explanation: https://www.youtube.com/watch?v=__98uL6wst8&t=572s
"""


class Solution:
    def numIslands(self, grid) -> int:
        """
        We are visiting each cell and if a cell is "1" then it is land, we use DFS to recursively find the surrounding
        land and mark it as visited by marking it as "2" and return if there is water "0" or visited "2".

        Simultaneously, we are incrementing the number of islands before each recursive call as that indicates a new
        island.

        :param grid:
        :return: num_of_islands
        """
        m = len(grid)  # Number of rows.
        n = len(grid[0])  # Number of columns.
        num_of_islands = 0  # Number of islands.
        for row in range(m):
            for column in range(n):
                if grid[row][column] == "1":  # If a land is found.
                    num_of_islands += 1  # Increment number of islands.
                    self.visit_island(grid, row, column)  # Visit the nearby cells to find how big the land is and mark.

        return num_of_islands

    def visit_island(self, grid, row, column):
        """
        Visit all the cells next to the land found ("1") and mark it all as visited.
        :param grid:
        :param row:
        :param column:
        :return: grid
        """
        m = len(grid)
        n = len(grid[0])
        if row < 0 or row > m - 1 or column < 0 or column > n - 1:  # If exceeding the length of the grid, return.
            return
        if grid[row][column] == "0":  # If water found, return.
            return
        if grid[row][column] == "2":  # If visited, return.
            return
        if grid[row][column] == "1":  # If not visited, mark as visited.
            grid[row][column] = "2"
        print("row", row, "column", column)
        # Do recursive call in all 4-Directions to check the size of the island.
        self.visit_island(grid, row + 1, column)
        self.visit_island(grid, row - 1, column)
        self.visit_island(grid, row, column + 1)
        self.visit_island(grid, row, column - 1)

        return grid


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
execute = Solution()
print(execute.numIslands(grid))
