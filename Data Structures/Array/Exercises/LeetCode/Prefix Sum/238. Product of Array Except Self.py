"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    # This fails due to time limit exceeded. But solution is straightforward, the left and right is calculated for each
    # number and added together.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        current = 0
        answer = []
        left_prod = 1
        right_prod = 1

        while current <= len(nums) - 1:
            # print(left, right, current, left_prod, right_prod, answer)
            if left < current:
                left_prod = left_prod * nums[left]
                left += 1
            elif right > current:
                right_prod = right_prod * nums[right]
                right -= 1
            else:
                answer.append(left_prod * right_prod)
                current += 1
                left_prod = 1
                right_prod = 1
                left = 0
                right = len(nums) - 1
        return answer

    def productExceptSelfOptimized(self, nums: List[int]) -> List[int]:
        """
        In this solution, the product from left to right is calculated, and then product from right to left is
        calculated, then we calculate the answer as a product of left product and right product.
        :param nums:
        :return: answer
        """
        left_prod = len(nums) * [1]
        right_prod = len(nums) * [1]
        answer = len(nums) * [1]

        left_prod[0] = nums[0]

        # Calculate left product.
        for i in range(1, len(nums)):
            left_prod[i] = left_prod[i - 1] * nums[i]

        # Calculate right product.
        for i in range(len(nums) - 1, 0, -1):
            right_prod[i - 1] = right_prod[i] * nums[i]

        # Calculate the product for each index in the nums array.
        answer[0] = right_prod[0]
        for i in range(1, len(answer)):
            answer[i] = left_prod[i - 1] * right_prod[i]

        return answer


nums = [1,2,3,4]
execute = Solution()
print(execute.productExceptSelfOptimized(nums))
