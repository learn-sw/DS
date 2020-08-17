# 
# unbounded knapsack: multiple occurance's of same item is allowed
# 
# 0-1 knapsack rec logic: max(v[size-1] +  knapsack(w, v, capacity-w[size-1], size-1), knapsack(w, v, capacity, size-1))


# unbounde knapsack logic: max( v[size-1] + unbounded_kp(w, v, cap-w[size-1], size),  unbounded_kp(w, v, cap, size-1))
# DP 
# i == 0 or j == 0:
    dp_arr[i][j] = 0
# if wt[i-1] <= j:
    dp_arr[i][j] = max(val[i-1] + dp_arr[i][j-wt[i-1]], dp[i-1][j]]
# if wt[i-1] <= j:
    dp_arr[i][j] = dp[i-1][j]