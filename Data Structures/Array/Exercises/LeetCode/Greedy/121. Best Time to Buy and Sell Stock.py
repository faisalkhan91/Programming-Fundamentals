"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan&id=level-1

Alternative solution can also be implemented using kadane's algorithm.
"""


class Solution:
    def maxProfit(self, prices):
        # If there is only one element in the list return 0.
        if len(prices) < 2:
            return 0

        buy = prices[0]  # Set the first element in array as assumed buy.
        profit = 0  # Profit set to 0.

        for i in range(1, len(prices)):  # Run loop from second element in array.
            if prices[i] < buy:  # If the current element in the array has lesser value than buy, make it the buy.
                buy = prices[i]
            elif prices[i] - buy > profit:  # Check if the sell and buy prices are greater than current profit.
                profit = prices[i] - buy
            # print("buy", buy, "profit", profit)
        return profit  # Return the current profit, if no profit it will return 0.


prices = [7, 1, 5, 3, 6, 4]
execute = Solution()
print(execute.maxProfit(prices))
