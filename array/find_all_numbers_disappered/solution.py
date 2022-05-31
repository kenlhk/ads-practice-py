"""
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.
"""


def findDisappearedNumbers(nums):

    # change all non-repeating number to negative, the duplicated number remains positive
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = -abs(nums[index])
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]


print(findDisappearedNumbers([1, 1]))
print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
