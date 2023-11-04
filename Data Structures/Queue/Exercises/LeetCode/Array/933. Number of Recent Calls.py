"""
933. Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75
"""


class RecentCounter:

    def __init__(self):
        self.pings = []  # This will be dequeue() instead of [] if using dequeue in python.

    def ping_initial(self, t: int) -> int:
        self.pings.append(t)
        count = 0

        for i in self.pings:
            if t - 3000 <= i <= t:
                count += 1

        return count

    def ping(self, t: int) -> int:
        self.pings.append(t)
        while self.pings and t - self.pings[0] > 3000:
            self.pings.pop(0)

        return len(self.pings)

    def ping_dequeue(self, t: int) -> int:
        self.pings.append(t)
        while self.pings and t - self.pings[0] > 3000:
            self.pings.popleft()

        return len(self.pings)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

t = [[], [1], [100], [3001], [3002]]
execute = RecentCounter()
print(execute.pings(t))
