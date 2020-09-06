# https://www.geeksforgeeks.org/binary-search/
 # ps: Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

# Binary Search: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

# inputs arr = [ 2, 3, 4, 10, 40 ] 
# x = 10

# output: 3

def binary_search(arr, ele):
    
    if len(arr) == 0:
        raise Exception("array is empty")
    
    min = 0
    max = len(arr) - 1

    while min <= max:
        mid = min + (max-min)//2
        if ele == arr[mid]:
            return mid
        elif ele > arr[mid]:
            min = mid + 1
        else:
            max = mid - 1


    return -1

arr = [ 2, 3, 4, 10, 40 ] 
x = 10


print(binary_search(arr, x))

arr = [] 
x = 10
print(binary_search(arr, x))
