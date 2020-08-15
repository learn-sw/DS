def reverse_sting(st):
    print(type(st))
    if type(st) is not str:
        raise TypeError("send valid sting")
    if len(st)==0:
        return st
    return reverse_sting(st[1:]) + st[0]

#print(reverse_sting("tarun"))
#print(reverse_sting(123))
def isPalindromerec(st, fi, li):
    
    if st[fi] != st[li]:
        return false
    if fi <= li :
        return isPalindromerec(st, fi+1, li-1 )

def isPalindrome(st):
    if len(st)>0:
        return isPalindromerec(st, 0, len(st)-1)
    else:
        raise Error("empty sting")


print(isPalindrome("121"))
        
