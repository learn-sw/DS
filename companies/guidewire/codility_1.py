# Given a string S consisting of N letters a and b. In one move you can replace one letter by the other (a by b or b by a).

# Write a function solution that given such a string S, returns the minimum number of moves required to obtain a string containing no instances of three identical consecutive letters.

# Example 1:

# Input: "baaaaa"
# Output: 1
# Explanation: The string without three identical consecutive letters which can be obtained is one move is "baabaa".
# Example 2:

# Input: "baaabbaabbba"
# Output: 2
# Explanation: There are four valid strings obtainable in two moves, for example "bbaabbaabbaa".
# Example 3:

# Input: "baabab"
# Ouput: 0
# Assumptions:

# N is an integer within the range [0, ..200,000];
# string S consists of only characteres a and b


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    
    result = 0 
    if len(S) == 0:
        return result
 
    t_len = 1
s = 'baaabbaabbba'
    for i in range(len(S)-1):

        if S[i] != S[i+1]:
            t_len = 1
            continue
        elif S[i] == S[i+1]:
            t_len +=1
        
        if(t_len==3):
            result+=1
            t_len = 0
            continue

    
    return result

print(solution(s))