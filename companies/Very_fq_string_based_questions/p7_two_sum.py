# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 105
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# 0 ~ 6 months6 months ~ 1 year1 year ~ 2 years

# Amazon 123 Google 74 Apple 53 Adobe 46 Facebook 30 Microsoft 28 Bloomberg 16

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # result = []
        # for i in range(len(nums)):         
        #     for j in range(i+1, len(nums)): 
        #         if target - nums[i] == nums[j]:
        #             return [i,j]
        
        dict = {}
        # for i in range(len(nums)):
        #    dict[nums[i]]= i

        
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict:
                return [dict[diff], i]
            else:
                dict[nums[i]] = i
