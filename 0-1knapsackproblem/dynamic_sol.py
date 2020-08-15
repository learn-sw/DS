# ###################### #
# Dynamic  solution   #
# ###################### # 

def dynamic_knapsack(w, v, capacity, n):
    
    # if len(w)<=0 or capacity <= 0:
    #     return 0

    item_size, bag_cap = (n+1, capacity+1)
    K_arr = [[-1 for x in range(bag_cap)] for x in range(item_size)] 
    print K_arr
    for i in range(n+1):
        for j in range(capacity+1):
            if i == 0 or j == 0:
                K_arr[i][j]=0
            elif w[i-1]<=j:
                K_arr[i][j] = max(v[i-1] + K_arr[i-1][j-w[i-1]], K_arr[i-1][j])
            elif w[i-1]>j:
                K_arr[i][j] = K_arr[i-1][j]

                
        print K_arr
    return K_arr[n][capacity]
    # top down approach create an array and initialize with basic conditions

w1 = [1,3,4,5]
v1 = [1,4,5,7]
cap = 7
n = len(w1) 
print(dynamic_knapsack(w1,v1,cap,n))