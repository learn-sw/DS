# i/p:
# arr : 2,1,2,3
# diff = 1
# o/p = 2



# problem statement: get min sub sets for a given array
def count_subset_sum(a, w, size):
    rows, cols = (size+1, w+1)
    dp_arr = [[0 for x in range(cols)] for x in range(rows)]
    
    for i in range(rows):
        for t_w in range(cols):
            if t_w==0:
                dp_arr[i][t_w] = 1
            elif t_w < a[i-1]:
                dp_arr[i][t_w] = dp_arr[i-1][t_w]
            elif t_w >= a[i-1]:
                dp_arr[i][t_w] = dp_arr[i-1][t_w] + dp_arr[i-1][t_w-a[i-1]]
        print(dp_arr)
    #dp_arr[size][w]
    return dp_arr[size][w]

def dp_count_nof_subset_with_given_diff(a, m_diff):

    su = sum(a)
    w = int((m_diff + su)/2)
    print(w)
    return(count_subset_sum(a, w, len(a)))


arr= [1,1,2,3]
min_diff = 1
print(dp_count_nof_subset_with_given_diff(arr, min_diff))
