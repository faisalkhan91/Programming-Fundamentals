"""
1679. Max Number of K-Sum Pairs
https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        operations = 0

        while left < right:
            if nums[left] + nums[right] == k:
                operations += 1
                left += 1

            if nums[left] > k:
                left += 1
            else:
                right -= 1

        return operations

    class Solution:
        def maxOperations(self, nums: List[int], k: int) -> int:

            nums_map = Counter(nums)
            print(nums_map)
            left = 0
            right = 0
            operations = 0

            while left < len(nums_map):
                if nums_map[left] == nums_map[right]:
                    if nums_map[left] > 0 and nums_map[right] > 0:
                        nums_map[left] -= 1
                        nums_map[right] -= 1
                    else:
                        left += 1
                    right += 1

            return 0

        class Solution:
            def maxOperations(self, nums: List[int], k: int) -> int:

                nums_map = {}
                left = 0
                right = 0
                operations = 0

                for i in range(len(nums)):
                    if nums[i] in nums_map:
                        nums_map[nums[i]] += 1
                        if nums_map[nums[i]] == 2:
                            operations = 0
                            nums_map[nums[i]] = 0
                    else:
                        nums_map[nums[i]] = 1

                while left < right:
                    if nums_map[left] == nums[right]:
                        operations += 1
                        left += 1

                    right -= 1

                return operations

            class Solution:
                def maxOperations(self, nums: List[int], k: int) -> int:

                    left = 0
                    right = len(nums) - 1
                    operations = 0

                    while left <= right:
                        if nums[left] + nums[right] == k:
                            operations += 1
                            left += 1
                        elif nums[left] >= k:
                            left += 1

                        right -= 1

                    return operations

                class Solution:
                    def maxOperations(self, nums: List[int], k: int) -> int:

                        nums_map = Counter(nums)
                        operations = 0

                        print(nums_map)
                        nums = list(nums_map.keys())
                        print(nums)

                        left = 0
                        right = len(nums) - 1

                        while left < right:

                            if nums[left] + nums[left] == k and nums_map[nums[right]] >= 2:
                                operations = nums_map[nums[left]] / nums[left]
                                nums_map[nums[left]] = nums_map[nums[left]] % nums[left]
                            elif nums[right] + nums[right] == k and nums_map[nums[right]] >= 2:
                                operations = nums_map[nums[right]] / nums[right]
                                nums_map[nums[right]] = nums_map[nums[right]] % nums[right]
                            elif nums[left] + nums[right] == k:
                                operations = operations + min(nums_map[nums[left]], nums_map[nums[right]])
                                left += 1
                            print(nums_map)
                            right -= 1

                        return operations