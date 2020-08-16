# i/p:
# arr : 2 3 7 8 10
# sum = 11

# problem: fcheck if a subset exists with value equals the sum<11>
# o/p: true r false


# recursive sol:


def rec_subset(arr, sum, size):
   # prin(sum
    is_false = False
    if sum == 0:
        return True
    if size == 0 and sum != 0:
        return False

    elif arr[size-1]> sum:
        print(">>"+str(is_false))
        return rec_subset(arr, sum, size-1)
    elif arr[size-1] <= sum:
        print("<<"+str(is_false))
        return  rec_subset(arr, sum - arr[size-1],size-1) or rec_subset(arr, sum, size-1)

arr = [2,3,7,8,10]
sum = 11
size = len(arr)
print(rec_subset(arr, sum, size))

