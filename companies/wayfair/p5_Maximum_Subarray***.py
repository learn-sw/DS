# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    curr_sum = max_sum = nums[0]
    
    for i in range(1, n):
        curr_sum = max(nums[i], curr_sum+nums[i])
        max_sum = max(curr_sum,max_sum)
    
    return max_sum

nums =[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))