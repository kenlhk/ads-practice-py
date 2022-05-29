"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


def singleNumber(nums):
    ans = 0
    for n in nums:
        ans ^= n
    return ans


print(singleNumber([2, 2, 1]))
print(singleNumber([4, 1, 2, 1, 2]))
