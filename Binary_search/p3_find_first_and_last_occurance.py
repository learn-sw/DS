# https://www.geeksforgeeks.org/find-first-and-last-positions-of-an-element-in-a-sorted-array/

# FIND FIRST AND LAST POSITIONS OF AN ELEMENT IN A SORTED ARRAY:

# Given a sorted array with possibly duplicate elements, the task is to find indexes of first 
# and last occurrences of an element x in the given array.

# Example:

# Input : arr[] = {1, 3, 5, 5, 5, 5 ,67, 123, 125}    
#         x = 5
# Output : First Occurrence = 2
#          Last Occurrence = 5

def find_first_and_last_occurance(arr, ele):

    first = last = -1
    min = 0
    max = len(arr) - 1

    while(min <= max):

        mid = min + (max-min)//2

        if arr[mid] == ele:
            first = mid
            max = mid -1
        elif arr[mid] < ele:
            
            min = mid + 1
        else: 
            max = mid -1
        print("first:" +str(first))
        print("\n")

    min = 0
    max = len(arr) - 1
    while(min <= max):

        mid = min + (max-min)//2
        if arr[mid] == ele:
            last = mid
            min = mid + 1
        elif arr[mid] < ele:
            min = mid + 1
        else: 
            max = mid -1
        print("last:" +str(last))
        print("\n")


    return(first, last)

arr = [1, 3, 5, 5, 5, 5 ,67, 123, 125]
x = 5
print(find_first_and_last_occurance(arr,x))