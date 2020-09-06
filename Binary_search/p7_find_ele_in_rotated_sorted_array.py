# https://leetcode.com/problems/search-in-rotated-sorted-array/
# FIND AN ELEMENT IN A ROTATED SORTED ARRAY:

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

def search(nums, target):
    ele_index = -1

    start, last  = 0, len(nums)-1
    
    while start <= last:

        mid = start + (last-start)//2
        if nums[mid] == target:
            return mid
        
        # if  sorted sub array is on left hannd side
        elif nums[start] <= nums[mid]:
            if target >= nums[start] and target <nums[mid]:
                last = mid-1
            else:
                start = mid +1
        # if sorted sub array is on right hannd side
        elif nums[mid] < nums[last]:
            if target > nums[mid] and target <= nums[last]:
                start = mid +1
            else:
                last = mid -1

    return ele_index
    

nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))

nums = [4,5,6,7,0,1,2]
target = 3
print(search(nums, target))

nums = [1]
target = 0
print(search(nums, target))