# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:

# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        list = []
        
        for num in nums:
            
            
            if len(list)==0 or num < list[-1]:
                list.append(num)
            else:
                list = [num] + list
                
            if len(list)>k:
                list.pop(list.index(min(list)))
                #list.remove(min(list))

        return min(list)