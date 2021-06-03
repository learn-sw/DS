#https://leetcode.com/problems/sort-colors/

# Given a string with lowercase, uppercase and numbers, rearrange it so that uppercase letters are first, then lowercase and then numbers. It should maintain the original order.

# Input- "cdBnC52c" output - "BCcdnc52"
# Input - "123abA" output - "Aab123"

# Rearrange it in o(n) in one pass without using extra space.

#class Solution(object):
def rearrange(input_str):

    input_str = list(input_str)
    p_up = curr = 0
    p_num = len(input_str)-1

    while curr <= p_num:
        print(input_str[curr], input_str)
        if input_str[curr].isupper():
            input_str[p_up], input_str[curr] = input_str[curr], input_str[p_up]
            curr +=1
            p_up +=1

        elif input_str[curr].isdigit():
            input_str[p_num], input_str[curr] = input_str[curr], input_str[p_num]
            p_num -=1
        else:
            curr +=1
    return ''.join(input_str)

input = "cdBnC52c"
print(rearrange(input))


