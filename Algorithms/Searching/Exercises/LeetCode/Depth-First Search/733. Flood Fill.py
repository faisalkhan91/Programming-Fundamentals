"""
733. Flood Fill
https://leetcode.com/problems/flood-fill/
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        return self.modified_image(image, sr, sc, color)

    def modified_image(self, image, row, column, color):
        m = len(image)
        n = len(image[0])
        if row < 0 or row > m - 1 or column < 0 or column > n - 1 or image[row][column] == color or image[row][
            column] == 0:
            return
        print("row", row, "column", column)
        image[row][column] = color
        self.modified_image(image, row + 1, column, color)
        self.modified_image(image, row - 1, column, color)
        self.modified_image(image, row, column + 1, color)
        self.modified_image(image, row, column - 1, color)

        return image
