"""
735. Asteroid Collision
https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        after_collision = [asteroids[0]]

        for asteroid in asteroids[1:]:
            if asteroid * after_collision[-1] < 0:
                if abs(asteroid) >= abs(after_collision[-1]):
                    after_collision.pop()
            else:
                after_collision.append(asteroid)

        return after_collision

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        after_collision = [asteroids[0]]

        for asteroid in asteroids[1:]:
            if asteroid * after_collision[-1] < 0 and after_collision[-1] > 0:
                print(asteroid)
                if abs(asteroid) >= after_collision[-1]:
                    tmp = after_collision.pop()
                    if sum(after_collision) < 0 and abs(tmp) != abs(asteroid):
                        after_collision.append(asteroid)
            else:
                after_collision.append(asteroid)
            print(after_collision)

        return after_collision
