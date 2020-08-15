
temp_val = []
def printComb(st, r_ele):
    if len(st)==0:
        return ""
    if len(st) < r_ele:
        return
        

    x = st[0:r_ele]
    
    if x not in temp_val:
        temp_val.append(x)
    printComb(st[1:],r_ele)
    return temp_val
    

printComb("12345", 3)
print(temp_val)