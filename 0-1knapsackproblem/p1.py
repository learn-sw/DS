
def knapsack(w, v, capacity, size):

    if capacity == 0 or size==0:
        return 0

    if  w[size-1] > capacity:
        return knapsack(w, v, capacity, size-1)
        
    else:
        return max(v[size-1] +  knapsack(w, v, capacity-w[size-1], size-1), knapsack(w, v, capacity, size-1))
        
    # items[] :     I1      I2      I3      I4 
    # weight[]:     1       3       4       5
    # value[]       1       4       5       7
w = [1,3,4,5]
v = [1,4,5,7]
cap = 11
size = len(w)
#print(knapsack(w,v,cap,size)) 


#   ###################### 
#   memoization solution
#   problem: stack uses with recursion prg
#   ######################

size, capacity = (5,12)
arr = [[-1]*capacity]*size

def memoize_knapsack(w, v, capacity, size):

    if capacity == 0 or size==0:
        return 0
    if arr[size][capacity]!= -1:
        return arr[size][capacity]

    if  w[size-1] > capacity:
        arr[size][capacity] = memoize_knapsack(w, v, capacity, size-1)
        return arr[size][capacity]
    else:
        arr[size][capacity] = max(v[size-1] +  memoize_knapsack(w, v, capacity-w[size-1], size-1), memoize_knapsack(w, v, capacity, size-1))
        return arr[size][capacity]

    # items[] :     I1      I2      I3      I4 
    # weight[]:     1       3       4       5
    # value[]       1       4       5       7
w = [1,3,4,5]
v = [1,4,5,7]
cap = 11
size = len(w)
#print(memoize_knapsack(w,v,cap,size))


