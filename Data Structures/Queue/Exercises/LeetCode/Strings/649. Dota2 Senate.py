"""
649. Dota2 Senate
https://leetcode.com/problems/dota2-senate/description/?envType=study-plan-v2&envId=leetcode-75
"""

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        radiant, dire = deque(), deque()
        length = len(senate)

        for i in range(length):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                dire.popleft()
                radiant.append(radiant.popleft() + length)
            else:
                radiant.popleft()
                dire.append(dire.popleft() + length)

        return "Radiant" if radiant else "Dire"


senate = "RD"
execute = Solution()
print(execute.predictPartyVictory(senate))
