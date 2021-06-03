# 1. Find all palindromic substrings of a given string < https://leetcode.com/discuss/interview-question/619517/Amazon-or-Phone-or-Find-all-palindromic-substrings-of-a-given-string>



def palnidrone_substring_count(s, i, j):
    
    count = 0
    
    if j>=len(s):
        return count    

    while s[i]==s[j]:          
        count +=1
        if i>=1 and j<=len(s)-2:
            i, j = i-1, j+1
        else:
            break 
    return count
    
    
def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    count = 0
    for index in range(len(s)):
        # if even
        count += palnidrone_substring_count(s, index, index+1)          
        # if odd
        count += palnidrone_substring_count(s, index, index)            
    return count

s = "abccb"
print(countSubstrings(s))