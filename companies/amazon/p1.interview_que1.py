# //List of strings ("","5","-2","4","Z","X","9","+","+")
# // sum of the numbers return
# // if it is "Z" remove last from result
# // if X multply last number by 2 and then add to result
# // if + , add last two values and then add it to result


def helper(li):
    result = 0
    prev = current = None
    for i in range(len(li)):
        if li[i].isdigit() or li[i].lstrip('-').isdigit():
            # print(li[i])
            prev = current
            current = int(li[i])
            result +=  current
            print(prev, current, "digit", result)
             #print(result)
            prev = int(li[i])
        else:
            if li[i] == 'Z':
                
                result = result - current
                current = 0 
                print(result)
            elif li[i] == 'X':
                result = result + (current*2)
                print(result)
            elif li[i] == '+':
                print(prev, current)
                result = result + (prev+current)
                print("+",result)
            

    return result
    #def isdigit():

list_val = ["","5","-2","4","Z","X","9","+","+"]
print(helper(list_val))


