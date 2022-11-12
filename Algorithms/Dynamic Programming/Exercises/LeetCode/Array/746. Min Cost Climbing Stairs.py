"""
746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/?envType=study-plan&id=level-1
"""


class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        min_cost = [0] * (len(cost))
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]

        for i in range(2, len(cost)):
            min_cost[i] = cost[i] + min(min_cost[i - 2], min_cost[i - 1])

        return min(min_cost[-1], min_cost[-2])

    def minCostClimbingStairs_optimized_memory(self, cost) -> int:
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
