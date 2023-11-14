"""
649. Dota2 Senate
https://leetcode.com/problems/dota2-senate/description/?envType=study-plan-v2&envId=leetcode-75
"""

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        In this solution, two queues, radiant and dire are used to store the indexes of the radiant and dire senators
        respectfully. The queues are iterated over. The senator with the higher index between them is banned while
        the senator with lower index is added back to the queue with a higher index by adding with a constant like
        length of the string. The result is returned once either queue is exhausted.
        :param senate: string
        :return: Who wins the round, Radiant or Dire
        """

        radiant, dire = deque(), deque()  # Initialize both the queues.
        length = len(senate)

        # Store the indexes of the senators in their respective queues.
        for i in range(length):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)

        # Iterate over the queues and update the rounds by adding the remaining senator back to the queue.
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
