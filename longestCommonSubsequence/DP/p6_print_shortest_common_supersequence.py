# ps:Printing Shortest Common Supersequence
#
# Given two strings X and Y, print the shortest string that has both X and Y as subsequences. If multiple shortest supersequence exists, print any one of them.

# Examples:

# Input: X = "AGGTAB",  Y = "GXTXAYB"
# Output: "AGXGTXAYB" OR "AGGXTXAYB" 
# OR Any string that represents shortest
# supersequence of X and Y

# Input: X = "HELLO",  Y = "GEEK"
# Output: "GEHEKLLO" OR "GHEEKLLO"
# OR Any string that represents shortest 
# supersequence of X and Y

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

    print(dp_arr)
    return dp_arr[n][m]

def dp_shortest_common_supersequence(x,y, n, m):
    dp_len = dp_len_longest_common_subsequence(s1, s2, len(s1), len(s2))
    return ((len(s1)+len(s2)) - dp_len)

s1 = "geeksforgeeks"
print(dp_longest_palindromic_subsequence(s1, len(s1)))
print("min del:" + str(dp_min_deletion_to_make_palindrome(s1, len(s1))))





