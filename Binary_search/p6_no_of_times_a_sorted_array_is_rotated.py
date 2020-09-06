# https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/

# Consider an array of distinct numbers sorted in increasing order. The array has been rotated (clockwise) k number of times. Given such an array, find the value of k.

# Examples:

# Input : arr[] = {15, 18, 2, 3, 6, 12}
# Output: 2
# Explanation : Initial array must be {2, 3,
# 6, 12, 15, 18}. We get the given array after 
# rotating the initial array twice.

# Input : arr[] = {7, 9, 11, 12, 5}
# Output: 4

# Input: arr[] = {7, 9, 11, 12, 15};
# Output: 0

def countRotations(arr):
    min = 0
    max = len(arr) -1
    if max == 0:
        return 0

    while min <=max:
        mid = min + (max - min)//2

        # if arr of mid is less than arr mid-1
        # the return arr[mid]
        if  mid > min and arr[mid] < arr [mid-1]:
            return mid
        # if arr of mid+1 is less than arr mid
        # the return arr[mid+1]
        if mid < max and arr[mid+1] < arr [mid]:
            return mid +1
        else: 
            # if arr[mid] > arr[max] then the ele will be in right side
            # min = mid +1
            if arr[mid] > arr[max]:
                min = mid +1
            else:
                max = mid -1

    return 0



arr = [15, 18, 2, 3, 6, 12] 
print(countRotations(arr))
arr = [7, 9, 11, 12, 5]
print(countRotations(arr))
arr = [7, 9, 11, 12, 15]
print(countRotations(arr))


