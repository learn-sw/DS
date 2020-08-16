# i/p:
# arr : 1, 6, 11, 5
# sum = 11
# o/p = 1



# problem statement: get min sub sets for a given array

import sys
def dp_subset(arr, sum,size):
    rows,cols = (size+1, sum+1)
    dp_arr = [[False for x in range(cols)] for x in range(rows)]

    for i in range(rows):
        for t_sum in range(cols):
            if t_sum == 0:
                dp_arr[i][t_sum] = True
            elif t_sum < arr[i-1]:
                dp_arr[i][t_sum] = dp_arr[i-1][t_sum]
            elif t_sum >= arr[i-1]:
                dp_arr[i][t_sum] = dp_arr[i-1][t_sum] or dp_arr[i-1][t_sum - arr[i-1]]
    return dp_arr

def dp_count_noof_subsets(a, sz):

    su = sum(a)
    dp_arr = dp_subset(a, su, sz)

    diff = sys.maxsize

    for j in range(len(dp_arr[0])//2):
        if dp_arr[sz][j] == True:
            diff = min(diff, su - (2*j))
            print(diff)

    return(diff)

    
arr = [1,2, 6, 11, 5]
nsize = len(arr)
print(dp_count_noof_subsets(arr, nsize))