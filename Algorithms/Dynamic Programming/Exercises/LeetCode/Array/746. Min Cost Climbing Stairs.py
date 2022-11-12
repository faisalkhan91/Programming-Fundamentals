"""
746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/?envType=study-plan&id=level-1
"""


class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        """
        This method counts the minimum cost associated with climbing stairs to the top of the staircase. Here we use
        dynamic programming bottom-up approach to calculate the cost associated to climb each stair with constraints
        being that each climb can be done in 1 or 2 steps.

        We declare an array to store the minimum cost associated with climb, we calculate the cost of first 2 steps
        manually and use the expression below to calculate the rest. We can, return the least of the last 2 values
        calculated as the last step can be skipped if we jump 2 stairs.

        Time complexity is O(n). Space complexity is O(n).
        :param cost:
        :return:
        """
        min_cost = [0] * (len(cost))  # Initialize minimum cost array.
        min_cost[0] = cost[0]  # Cost of the first step is same as in the cost array.
        min_cost[1] = cost[1]  # Cost of the second step is same as in the cost array.

        for i in range(2, len(cost)):
            # Here, minimum cost for the current step is cost of the current step plus lowest of the minimum cost
            # calculated to reach the last two steps.
            min_cost[i] = cost[i] + min(min_cost[i - 2], min_cost[i - 1])

        return min(min_cost[-1], min_cost[-2])  # Return the lowest of the last 2 costs as we can skip 1 step.

    def minCostClimbingStairs_optimized_memory(self, cost) -> int:
        """
        This is similar to above but is cost optimized towards memory consumption and the space complexity is O(1) as we
        use constant variables.
        :param cost:
        :return:
        """
        min_cost_current = min(cost[0], cost[1])
        min_cost_0 = cost[0]
        min_cost_1 = cost[1]

        for i in range(2, len(cost)):
            min_cost_current = cost[i] + min(min_cost_0, min_cost_1)
            min_cost_0, min_cost_1 = min_cost_1, min_cost_current

        return min(min_cost_current, min_cost_0)


cost = [4, 1]
execute = Solution()
print(execute.minCostClimbingStairs_optimized_memory(cost))
