"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
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


nums = [1,2,3,4]
execute = Solution()
print(execute.productExceptSelf(nums))
