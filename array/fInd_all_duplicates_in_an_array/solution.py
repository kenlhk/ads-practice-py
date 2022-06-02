"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
"""


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        ans = []
        # marked the linked number as negative in first occurrence
        for n in nums:
            if nums[abs(n) - 1] < 0:
                ans.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1
        return ans


solution = Solution()
print(solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
print(solution.findDuplicates([1, 1, 2]))
