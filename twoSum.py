"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""


class Solution(object):
    def twoSum(self, nums, target):
        numsLength = len(nums)
        for i in range(numsLength):
            for j in range(numsLength):
                       if target == nums[i] + nums[j] and i!=j:
                            result = [i, j]
                            return result
                       