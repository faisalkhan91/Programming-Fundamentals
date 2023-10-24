"""
735. Asteroid Collision
https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        """
        In this solution stack is used to track the collision of the asteroids. The stack is checked for each asteroid
        (using a while loop) since the asteroids are in a row and collisions only occur when a -ve asteroid is detected.
        the remaining asteroids are returned after collisions.

        Time Complexity: O(n^2), Space Complexity: O(n).
        """
        after_collision = []  # This is a stack that stores the surviving asteroids after each collision.

        for asteroid in asteroids:
            # We check the full stack for each asteroid as there can be multiple collisions. The conditions checked are
            # if there is an asteroid in the stack and if the previous asteroid is +ve (i.e., it is moving to the right)
            # and the current asteroid is moving to the left as this will cause collision.
            while after_collision and after_collision[-1] > 0 > asteroid:
                if after_collision[-1] < abs(asteroid):  # If the previous asteroid is small, it will be destroyed.
                    after_collision.pop()
                    continue  # This will not check any other conditions and go back to the start of the while loop.
                elif after_collision[-1] == abs(asteroid):  # If the asteroid's values are similar, both are destroyed.
                    after_collision.pop()
                break  # Break out of the loop if the conditions are not met anymore.
            else:
                after_collision.append(asteroid)  # Add asteroids to the stack if they are not colliding.

        return after_collision


asteroids = [5,10,-5]
execute = Solution()
print(execute.asteroidCollision(asteroids))
