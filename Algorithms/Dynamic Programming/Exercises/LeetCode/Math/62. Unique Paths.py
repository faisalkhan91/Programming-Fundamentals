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

    # Brute force alternative approach. In this approach a grid is initialized with m and n and the bottom right corner
    # is set to 1. Then a nested method is used to loop through the grid recursively until it reaches the bottom right
    # corner. It has the same pitfall as the above method as in once the grid gets large enough the algorithm fails.
    def uniquePaths_bruteforce_2(self, m: int, n: int) -> int:
        completed_paths = [0]
        grid = [[0 for i in range(n)] for j in range(m)]  # Initialize a 2D array of size m x n.
        grid[m - 1][n - 1] = 1  # Set the bottom right corner to 1.

        def routes(i, j):
            if i > m - 1 or j > n - 1:  # If the indexes are out of range stop processing.
                return
            if grid[i][j] == 1:  # If the bottom right corner is reached, save the path.
                completed_paths[0] += 1
                return
            routes(i + 1, j)
            routes(i, j + 1)
        routes(0, 0)  # Start from the top left corner.
        return completed_paths[0]

    # Reference: https://www.youtube.com/watch?v=IlEsdxuD4lY
    # This approach is basically calculating paths from each cell and summing them up as we move towards the start of
    # grid. This is a math approach.
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n  # Setting all the cells in the row to 1.
        for i in range(m - 1):
            new_row = [1] * n  # Initialize the new row to 1.
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j]  # Calculate the values of the new row based on the previous row.
            row = new_row  # Set the calculated row as the previous row.
        return row[0]

    # In this solution we use dynamic programming to store the values of each path from the current cell.
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1 for i in range(n)] for j in range(m)]  # Declare the matrix with all values as 1.
        for row in range(1, len(matrix)):  # Get the row
            for column in range(1, len(matrix[row])):  # Get the column in each row
                # Calculate the path from value from the row cell before and column cell above for each cell.
                matrix[row][column] = matrix[row - 1][column] + matrix[row][column - 1]
        return matrix[m - 1][n - 1]  # Return the end cell value.


m = 2
n = 3
execute = Solution()
execute.uniquePaths(m, n)
