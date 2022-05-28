"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
"""


def missingNumber(nums):
    sum = 0
    for n in nums:
        sum ^= n
    for i in range(len(nums) + 1):
        sum ^= i
    return sum


print(missingNumber([3, 0, 1]))
print(missingNumber([0, 1]))
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
