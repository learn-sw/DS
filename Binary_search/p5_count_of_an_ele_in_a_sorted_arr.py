
# https://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/
# COUNT NUMBER OF OCURRENCES(or frequency) IN A SORTED ARRAY:

# Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[]. Expected time complexity is O(Logn)
# Examples:

#   Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 2
#   Output: 4 // x (or 2) occurs 4 times in arr[]

#   Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 3
#   Output: 1 

def count_frequency_of_an_ele(arr, ele):


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

    if last == -1:
        return 0

    return (last - first) +1


arr = [ 1, 1, 2, 2, 2, 2, 3 ] 
x = 2

print(count_frequency_of_an_ele(arr, x))

arr = [ 1, 1, 2, 2, 2, 2, 3 ] 
x = 5

print(count_frequency_of_an_ele(arr, x))

arr = [2] 
x = 2

print(count_frequency_of_an_ele(arr, x))

