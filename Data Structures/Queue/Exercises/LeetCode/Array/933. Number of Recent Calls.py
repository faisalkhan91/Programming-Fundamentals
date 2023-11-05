"""
933. Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75
"""

# from collections import deque


class RecentCounter:

    def __init__(self):
        self.pings = []  # This will be dequeue() instead of [] if using dequeue in python.

    def ping_initial(self, t: int) -> int:
        """
        This is the initial attempt of solving this problem. In this solution after appending the t to the list, the
        list is iterated to find all the elements between the range of t - 3000 and t and a count variable is used to
        store the elements in this range. Unfortunately, this solution was slow and did not complete all the test cases
        as iterating through large lists was slowing it down. This can be optimized by utilizing a queue as shown below.

        Time Complexity: O(n^2), Space Complexity: O(n).
        :param t: requests
        :return: count
        """
        self.pings.append(t)  # Append the ping.
        count = 0  # Initialize the count variable.

        for i in self.pings:  # Iterate through pings.
            if t - 3000 <= i <= t:
                count += 1

        return count

    def ping(self, t: int) -> int:
        """
        This solution uses the Queue datastructure to store the requests. Everytime there is a new request, the value is
        appended to the Queue, and all the values that do not fit the range of the new request are popped use the FIFO
        methodology of the Queue. The length of the current queue contains all the elements fitting the range.

        Time Complexity: O(n), Space Complexity: O(n).
        :param t: requests
        :return: length of the Queue
        """
        self.pings.append(t)
        while self.pings and t - self.pings[0] > 3000:  # If pings have values and value is not in range of last 3000 ms
            self.pings.pop(0)  # Remove the element from queue.

        return len(self.pings)

    def ping_dequeue(self, t: int) -> int:
        """
        This solution uses Queue datastructure, but uses the dequeue method implemented in python as opposed to the list
        used as above.

        Time Complexity: O(n), Space Complexity: O(n).
        This solu
        :param t:
        :return: length of the Queue
        """
        self.pings.append(t)
        while self.pings and t - self.pings[0] > 3000:
            self.pings.popleft()

        return len(self.pings)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

t = [[], [1], [100], [3001], [3002]]
execute = RecentCounter()
for i in t:
    if i:
        print(execute.ping(i[0]))
