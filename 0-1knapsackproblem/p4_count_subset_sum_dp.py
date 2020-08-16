# i/p:
# arr : 2 3 7 8 10
# sum = 11

# problem: get total number of sub sets for a give sum 
# o/p: true r false

# recursive sol:

def dp_count_noof_subsets(arr, sum, size):
    rows, cols =  (size+1, sum+1)
    dp_arr = [[0 for x in range(cols)] for x in range(rows)]

    for i in range(rows):
        for t_sum in range(cols):
            if t_sum == 0:
                dp_arr[i][t_sum] = 1
            elif arr[i-1] > t_sum:
                dp_arr[i][t_sum] = dp_arr[i-1][t_sum]
            elif arr[i-1] <= t_sum:
                dp_arr[i][t_sum] = dp_arr[i-1][t_sum] + dp_arr[i-1][t_sum-arr[i-1]]

    print(dp_arr)

    return dp_arr[size][sum]
arr = [2,3,5,6,8,10]
sum = 10
size = len(arr)
print(dp_count_noof_subsets(arr, sum, size))

