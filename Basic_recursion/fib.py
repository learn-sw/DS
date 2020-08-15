def fib(a):
    if (a <0):
        return "incorrect input"
    if(a==1):
        return 0
    elif (a ==2 ):
        return 1
    return fib(a-1) + fib(a-2)

# print(fib(5))


fibarr = [0,1]
def mfib(a):
    if (a<0):
        print('incorrect input')
    if (a <= len(fibarr)):
       # print ('a:'+str(a))
        return fibarr[a-1]

   # print ('a:'+str(a))
    # print ('temp:'+str(temp))
    temp = mfib(a-1) + mfib(a-2)
   # print ('temp:'+str(temp))
   # print ('a:'+str(a))
    print("temp valu::"+str(temp))
    fibarr.append(temp)
    return temp

print(mfib(50))

# 4
# fib(3)+ fib(2) == fib(3) + 1
# fib(3) + 1 = fib(2) + fib(1) + 1 = 1+ 0 +1 =2
# 0,1,1,2,3,5,8

# 5
# f(4) + f(3)
# f(3)+f(2) + f(2)+f(1)
# f(2) + f(1)+f(2) + f(2)+f(1)
# 1 + 0 +1 + 1 +0 = 3

# 6
# f(5)
# f(4) + f(3)
# f(3)+f(2) + f(2)+f(1)

# f(2) + f(1)++f(2) + f(2)+f(1)
# 1 0 1 1 0 = 3 + 2 = 5