# https://www.geeksforgeeks.org/search-almost-sorted-array/


# Given an array which is sorted, but after sorting some elements are moved to either of the adjacent positions, i.e., arr[i] may be present at arr[i+1] or arr[i-1]. Write an efficient function to search an element in this array. Basically the element arr[i] can only be swapped with either arr[i+1] or arr[i-1].

# For example consider the array {2, 3, 10, 4, 40}, 4 is moved to next position and 10 is moved to previous position.

# Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 40
# Output: 2 
# Output is index of 40 in given array

# Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 90
# Output: -1
# -1 is returned to indicate element is not present
def search(arr, ele):
    min, max = 0, len(arr)-1

    while min <= max:
        mid = min + (max - min)//2
        if arr[mid] == ele:
            return mid
        if mid-1 >= min and arr[mid-1] == ele:
            return mid-1
        if mid+1 <= max and arr[mid+1] == ele:
            return mid+1
        elif arr[mid] > ele:
            max = mid - 2
        else:
            min = mid +2
        
    return -1


arr =  [10, 3, 40, 20, 50, 80, 70]
key = 40
print(search(arr, key))

arr =  [10, 3, 40, 20, 50, 80, 70]
key = 90
print(search(arr, key))
arr =  [9]
key = 90
print(search(arr, key))