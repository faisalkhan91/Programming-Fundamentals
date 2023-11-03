"""
933. Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75
"""


class RecentCounter:

    def __init__(self):
        self.ping_count = []

    def ping(self, t: int) -> int:
        self.ping_count.append(t)
        range1 = [t - 3000, t]
        count = 0

        for i in self.ping_count:
            if i in range1:
                count += 1
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
