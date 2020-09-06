# https://www.geeksforgeeks.org/find-first-and-last-positions-of-an-element-in-a-sorted-array/

# FIND FIRST AND LAST POSITIONS OF AN ELEMENT IN A SORTED ARRAY:

# Given a sorted array with possibly duplicate elements, the task is to find indexes of first 
# and last occurrences of an element x in the given array.

# Example:

# Input : arr[] = {1, 3, 5, 5, 5, 5 ,67, 123, 125}    
#         x = 5
# Output : First Occurrence = 2
#          Last Occurrence = 5

def order_not_know_search(arr, ele):


    min = 0
    max = len(arr) - 1

    while(min <= max):

        mid = min + (max-min)//2

        if arr[mid] == ele:
            return mid
        
        elif arr[mid] < arr[mid+1]:
            if arr[mid] < ele:
                min = mid + 1
            else: 
                max = mid -1

        else:
            if ele > arr[mid]:
                max = mid - 1
            else:
                min = mid + 1
    return -1              

arr = [ 2, 3, 4, 10, 40 ] 
x = 10
print(order_not_know_search(arr, x))

arr = [ 40, 10, 5,3,1 ] 
x = 10

print(order_not_know_search(arr, x))