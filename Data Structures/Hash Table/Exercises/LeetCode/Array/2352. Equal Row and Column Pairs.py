"""
2352. Equal Row and Column Pairs
https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def equalPairs(self, grid) -> int:
        """
        In this solution, the transpose of the grid is created and the columns are stored in the column_map list. The
        rows and columns are compared to see if they form an equal pair, the count of the equal pairs is returned.
        """
        column_map = []  # To store the column transpose.
        count = 0
        length = len(grid)

        for row in range(length):
            col = []  # Reset column.
            for column in range(length):
                col.append(grid[column][row])  # Append the current elements in a column to the col list.
            column_map.append(col)

        for row in grid:
            for column in column_map:
                if row == column:  # To check if the rows and columns are equal.
                    count += 1

        return count


grid = [[3,2,1],[1,7,6],[2,7,7]]
grid1 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
execute = Solution()
print(execute.equalPairs(grid))
