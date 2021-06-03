# Given an array of integers, count number of subarrays (of size more than one) that are strictly increasing.
# Expected Time Complexity : O(n)
# Expected Extra Space: O(1)

# Examples:

# Input: arr[] = {1, 4, 3}
# Output: 1
# There is only one subarray {1, 4}

# Input: arr[] = {1, 2, 3, 4}
# Output: 6
# There are 6 subarrays {1, 2}, {1, 2, 3}, {1, 2, 3, 4}
#                       {2, 3}, {2, 3, 4} and {3, 4}

# Input: arr[] = {1, 2, 2, 4}
# Output: 2
# There are 2 subarrays {1, 2} and {2, 4}


def countIncreasing(arr, n): 
    if not arr:
        return 0
    
    len = 0
    temp_count = 1
    for index in range(1,n):
        if arr[index] >  arr[index-1]:
            len += temp_count
            temp_count +=1
        else:
            temp_count = 1
            index -=1

    return len

arr = [1, 2, 2, 4] 
n = len(arr)
countIncreasing(arr, n)

arr = [1, 2, 3, 4] 
n = len(arr)
countIncreasing(arr, n)

arr = [-1, 4, 3] 
n = len(arr)
print(countIncreasing(arr, n))

arr = [] 
n = len(arr)
print(countIncreasing(arr, n))

arr = [1] 
n = len(arr)
print(countIncreasing(arr, n))
