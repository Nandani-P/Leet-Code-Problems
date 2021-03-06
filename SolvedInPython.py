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
                       


"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = x
        if x < 0:
            x = -x
            
        x = str(x)
        x = list(x)
        res = ""
        for i in reversed(x):
            res = res + str(i)
      
        res = int(res)
           
        if y < 0 and res > 2147483647:
            return 0
        
        if y < 0:
            return -res
        
        if res > 2147483648:
            return 0 
        else:
            return res
            
"""Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x > 2147483647:
            return False
        x = str(x)
        listX = list(x)
        lenListX = len(listX)
        
        if lenListX == 2 and listX[0] !=listX[1]:
            return False
            
        if lenListX ==1:
            return True
        
        for i in range(lenListX//2):
            if listX[i] != listX[-(i+1)]:
                return False
        return True
        
            
            
        
