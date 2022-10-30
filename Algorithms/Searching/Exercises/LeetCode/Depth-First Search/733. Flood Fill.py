"""
733. Flood Fill
https://leetcode.com/problems/flood-fill/
"""


class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        """
        The method uses DFS to visit each pixel and make changes according to the conditions below. We increment or
        decrement the rows and columns and check for modification based on the preset conditions.
        """
        start = image[sr][sc]  # Store initial value of the starting pixel so we can compare other pixels like it.
        return self.modified_image(image, sr, sc, color, start)

    def modified_image(self, image, row, column, color, start):
        m = len(image)  # Calculate the number of rows.
        n = len(image[0])  # Calculate the number of columns.
        if row < 0 or row > m - 1 or column < 0 or column > n - 1:  # If the row or columns exceeds the index range.
            return
        if image[row][column] != start:  # If the pixel value does not match the start pixel
            return
        if image[row][column] == color:  # If the pixel already has the needed color.
            return image
        image[row][column] = color  # Set the new color for the current pixel.
        # Move the pixel 4-directionally using recursion as below.
        self.modified_image(image, row + 1, column, color, start)
        self.modified_image(image, row - 1, column, color, start)
        self.modified_image(image, row, column + 1, color, start)
        self.modified_image(image, row, column - 1, color, start)

        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2

execute = Solution()
print(execute.floodFill(image, sr, sc, color))
