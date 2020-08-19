# ps: Longest Palindromic Subsequence | DP-12

# Given a sequence, find the length of the longest palindromic subsequence in it.
# i/p: geeksforgeeks
# o/p 5 
# explaination: eekee, eesee, eefee

# As another example, if the given sequence is “BBABCBCAB”, then the output should
# be 7 as “BABCBAB” is the longest palindromic subsequence in it. “BBBBB” and “BBCBB”
# are also palindromic subsequences of the given sequence, but not the longest ones.

def dp_len_longest_common_subsequence(x,y, n, m):
    r,c = n+1, m+1

    dp_arr = [[ -1 for x in range(c)] for x in range(r)]

    for i in range(r):
        for j in range(c):

            if i == 0 or j ==0:
                dp_arr[i][j] = 0
            elif x[i-1] == y[j-1]:
                dp_arr[i][j] = 1 + dp_arr[i-1][j-1]
            else:
                dp_arr[i][j] = max(dp_arr[i][j-1], dp_arr[i-1][j])

    return dp_arr[n][m]

def dp_longest_palindromic_subsequence(s, n):
    return(dp_len_longest_common_subsequence(s,s[::-1], n, n))

def dp_min_deletion_to_make_palindrome(s,n):
    len_palindrome = dp_len_longest_common_subsequence(s,s[::-1], n, n)
    return n - len_palindrome

s1 = "geeksforgeeks"
print(dp_longest_palindromic_subsequence(s1, len(s1)))
print("min del:" + str(dp_min_deletion_to_make_palindrome(s1, len(s1))))

s1 = "agbcba"
print(dp_longest_palindromic_subsequence(s1, len(s1)))
print("min del:" + str(dp_min_deletion_to_make_palindrome(s1, len(s1))))


s1 = ""
print(dp_longest_palindromic_subsequence(s1, len(s1)))
print("min del:" + str(dp_min_deletion_to_make_palindrome(s1, len(s1))))



