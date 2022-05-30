"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


class Solution:

    # the product of each element is equal to the product of the first half array and the second half
    # except the self
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = []
        acc = 1
        # 1. calculate the product of the first half array except the self
        for i in range(len(nums)):
            ans.append(acc)
            acc *= nums[i]

        acc = 1
        # 2. multiply the product of second half array in each element
        for i in reversed(range(len(nums))):
            ans[i] *= acc
            acc *= nums[i]

        return ans


solution = Solution();
print(solution.productExceptSelf([1, 2, 3, 4]))
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
