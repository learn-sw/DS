# i/p:
# arr : 2 3 7 8 10
# sum = 11

# problem: check if a subset exists with value equals the sum<11>
# o/p: true r false


# recursive sol:


def rec_eqsum_subset(arr, sum, size):


arr = [2,3,7,8,10]
sum = 11
size = len(arr)
print(rec_eqsum_subset(arr, sum, size))

