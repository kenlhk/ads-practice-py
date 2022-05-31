"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""


class Solution:

    # Not constant extra space, Time: O(n), Space: O(n)
    def findDuplicate(self, nums: list[int]) -> int:
        temp = set()
        for n in nums:
            if temp.__contains__(n):
                return n
            temp.add(n)

    # Floyd's tortoise and hare cycle detection, Time: O(n), Space: O(1)
    def findDuplicate2(self, nums: list[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]

        # # hare moves twice as fast as tortoise until they meet
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # tortoise back to starting point, hare keeps moving with same speed of tortoise
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return tortoise


solution = Solution();
print(solution.findDuplicate([1, 3, 4, 2, 2]))
print(solution.findDuplicate([3, 1, 3, 4, 2]))
print(solution.findDuplicate2([1, 3, 4, 2, 2]))
print(solution.findDuplicate2([3, 1, 3, 4, 2]))
