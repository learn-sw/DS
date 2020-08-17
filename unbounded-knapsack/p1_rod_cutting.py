# problem: max profit

# i/p
# length = 1 2 3 4  5  6  7 8 
# price  = 1 5 8 9 10 17 17 20
# N<len of rod>: 8 

# o/p: get max profit for a rod




def rod_cut_problem(arr_rod, pricearr, size, len_rod):
    rows, cols = size, len_rod+1 
    u_arr = [[-1 for x in range(cols)] for x in range(rows)] 

    for i in range(rows):
        for j in range(cols):
            if i == 0 or j == 0:
                u_arr[i][j]=0
            elif arr_rod[i-1] > j:
                u_arr[i][j]= u_arr[i-1][j]
            elif arr_rod[i-1] <= j:
                 u_arr[i][j]= max(u_arr[i-1][j],pricearr[i-1]+ u_arr[i][j-arr_rod[i-1]])
        print(u_arr)
        print("\n")
    return u_arr[size-1][len_rod]

length_rod= [1, 2, 3, 4,  5,  6,  7, 8 ]
lenth_price = [1, 5, 8, 9, 10, 17, 17, 20]
print(rod_cut_problem(length_rod,lenth_price, len(length_rod),len(length_rod)))