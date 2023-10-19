"""
2352. Equal Row and Column Pairs
https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        column_map = []
        temp = []
        count = 0

        for row in range(len(grid)):
            for column in range(len(grid)):
                temp.append(grid[column][row])
                if len(temp) % len(grid) == 0:
                    column_map.append(temp)
                    temp = []

        for row in grid:
            for column in column_map:
                if row == column:
                    count += 1

        return count


grid = [[3,2,1],[1,7,6],[2,7,7]]
grid1 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
execute = Solution()
print(execute.equalPairs(grid))
