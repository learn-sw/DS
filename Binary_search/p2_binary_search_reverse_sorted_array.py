# Let's suppose that we have an array sorted in descending order and we want to find index of an element e within this array. Binary search in every step picks the middle element (m) of the array and compares it to e. If these elements are equal, than it returns the index of m. If e is greater than m, than e must be located in the left subarray. On the contrary, if m greater than e, e must be located in the right subarray. At this moment binary search repeats the step on the respective subrarray.

# Because the algoritm splits in every step the array in half (and one half of the array is never processed) the input element must be located (or determined missing) in at most \\log_{2}{n} steps.

def binary_serach_reverse_sorted(arr, ele):

    min = 0
    max = len(arr) - 1
    while min <= max:
        mid = min + (max-min)//2
        if ele == arr[mid]:
            return mid
        elif ele > arr[mid]:
            
            max = mid - 1
        else:
            
            min = mid + 1

    return -1

arr = [ 40, 10, 5,3,1 ] 
x = 10


print(binary_serach_reverse_sorted(arr, x))