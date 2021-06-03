# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# 442. Find All Duplicates in an Array
# Medium

# 2785

# 162

# Add to List

# Share
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
#         nums_dict = {}
#         result =[]
        
#         for index in range(len(nums)):
#             if nums[index] not in nums_dict:
#                 nums_dict[nums[index]] = index
#             else:
#                 result.append(nums[index])
#         result = set(result)
#         return result
        res = []
        for num in nums:
            num = abs(num)

            if nums[num - 1] > 0:
                nums[num - 1] *= -1
            else:
                res.append(num)

        return res