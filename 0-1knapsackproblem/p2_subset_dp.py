# i/p:
# arr : 2 3 7 8 10
# sum = 11

# problem: fcheck if a subset exists with value equals the sum<11>
# o/p: true r false


# recursive sol:


def dp_subset(arr, sum, size):
    
    rows, cols = size+1, sum+1
    s_arr = [[False for x in range(cols)]for x in range(rows)]

    for n in range(rows):
        for wt in range(cols):
            if wt == 0:
                s_arr[n][wt]= True
            elif arr[n-1] > wt:
                s_arr[n][wt] = s_arr[n-1][wt]
            elif arr[n-1] <= wt:
                s_arr[n][wt] = s_arr[n-1][wt] or s_arr[n-1][wt- arr[n-1]]
    print(s_arr)
    #print(s_arr[size][sum])
    return s_arr[size][sum]     

arr = [2,3,7,8,10]
sum = 11
size = len(arr)
print(dp_subset(arr, sum, size))

