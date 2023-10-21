"""
735. Asteroid Collision
https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        after_collision = []
        previous_asteroid = 0

        for asteroid in asteroids:
            previous_asteroid = asteroid
            if previous_asteroid <= asteroid:
                after_collision.pop()
            after_collision.append(asteroid)

        return after_collision

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        after_collision = []
        previous_asteroid = asteroids[0]
        after_collision.append(asteroids[0])

        for asteroid in asteroids[1:]:
            if previous_asteroid < asteroid and previous_asteroid < 0:
                after_collision.pop()
                after_collision.append(asteroid)
            elif abs(previous_asteroid) == abs(asteroid):
                after_collision.pop()
            else:
                previous_asteroid = asteroid
                after_collision.append(asteroid)

        return after_collision