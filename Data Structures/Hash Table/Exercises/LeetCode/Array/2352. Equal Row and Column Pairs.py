"""
2352. Equal Row and Column Pairs
https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def equalPairs(self, grid) -> int:
        row_map = {}
        column_map = {}

        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         row_map[ij] = (grid[i], grid[j])

        for row in grid:
            row_map[str(row[0])] = 1

        print(row_map)
        return 0


grid = [[3,2,1],[1,7,6],[2,7,7]]
grid1 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
execute = Solution()
print(execute.equalPairs(grid))
