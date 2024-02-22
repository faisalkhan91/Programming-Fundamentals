"""
841. Keys and Rooms
https://leetcode.com/problems/keys-and-rooms/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = {0}
        i = 0

        while True:
            for keys in rooms[i]:
                visited.add(keys)

        print(visited)

        return True if len(rooms) == len(visited) else False