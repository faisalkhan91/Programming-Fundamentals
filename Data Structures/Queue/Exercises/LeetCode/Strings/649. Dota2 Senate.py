"""
649. Dota2 Senate
https://leetcode.com/problems/dota2-senate/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        queue = deque()

        if len(senate) <= 1:
            return "Dire" if senate == "D" else "Radiant"
        if senate[0] != senate[1]:
            queue.append(senate[0])
        else:
            queue.append(senate[0])
            queue.append(senate[1])

        for senator in senate[2:]:
            queue.append(senator)

            if queue[0] != senator:
                queue.popleft()
            print(queue)

        return "Dire" if queue[0] == "D" else "Radiant"
