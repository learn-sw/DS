# problem: minimum nmumber of coins to return the given sum
# i/p
# coin []: [1,2,3]
# sum: 5

# o/p: get min number of coins to get the given sum

import sys
def min_nof_coins_to_get_the_sum(coins, m_sum, size):
    
    
    rows, cols = size+1, m_sum+1 
    
    # initialize row [0]
    # if sum = 1 and arr[] is empty. possible number of coins to make the sum: infinite
    # so initialize the row[0] with maxInt -1
    uk_arr = [[0 for x in range(cols)] for x in range(rows)] 
    for j in range(cols):
        uk_arr[0][j] = sys.maxsize - 1 
    print(uk_arr)
    print("\n")

    # initialize 2nd row for this problem:
    for j in range(1,cols):
        if j % coins[0]  == 0:
            uk_arr[1][j] = int(j/coins[0])
        else:
            uk_arr[1][j] = sys.maxsize -1
    print(uk_arr)
    print("\n")

    for i in range(2, rows):
        for j in range(1,cols):
            if coins[i-1] > j:
                uk_arr[i][j] = uk_arr[i-1][j]
            elif coins[i-1] <=j:
                uk_arr[i][j] = min( 1 + uk_arr[i][j - coins[i-1]], uk_arr[i-1][j])

    print(uk_arr)
    return uk_arr[size][m_sum]
    
coins= [1,2, 3]
m_sum = 5
print(min_nof_coins_to_get_the_sum(coins, m_sum, len(coins)))


import sys







