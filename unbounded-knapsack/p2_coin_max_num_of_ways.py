# problem: max profit

# i/p
# coin []: [1,2,3]
# sum: 5

# o/p: get max number ways to get the given sum




def max_no_ways_to_get_the_sum(coins, m_sum, size):
    
    
    rows, cols = size+1, m_sum+1 
    
    
    
    u_arr = [[0 for x in range(cols)] for x in range(rows)] 
    
    for i in range(rows):
        u_arr[i][0] = 1


    for i in range(1, rows):
        for j in range(1, cols):

            if coins[i-1] > j:
                u_arr[i][j]= u_arr[i-1][j]

            elif coins[i-1] <= j:
                u_arr[i][j]= u_arr[i-1][j] + u_arr[i][j - coins[i-1]]

    return u_arr[size][m_sum]



coins= [1,2,3]
print(coins[-1])
m_sum = 5
print(max_no_ways_to_get_the_sum(coins, m_sum, len(coins)))


## 
# coins= [1,2,3]
# m_sum = 5


# 1 1 1 1 1 = 5
# 1 1 1 2 = 5
# 1 1 3 =5 

# 2 + 2 +1 = 5
# 2 + 3 = 5






