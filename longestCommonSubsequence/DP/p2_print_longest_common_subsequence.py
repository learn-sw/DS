# Given two sequences, print the longest subsequence present in both of them.
# Examples:
# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

# https://www.geeksforgeeks.org/printing-longest-common-subsequence/
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
    return dp_arr

def dp_print_longest_common_substring(x,y, n, m):
    p_arr = dp_len_longest_common_subsequence(s1, s2, len(s1), len(s2))
    p_str=""
    while (n>0 and m>0):
        if x[n-1] == y [m-1]:
            p_str += x[n-1]
            n -= 1
            m -=1
        else:
            if p_arr[n-1][m] > p_arr[n][m-1]:
                n -= 1
            else:
                m -=1
    return p_str[::-1]

s1 = "abcdxyz"
s2 = "zyabcd"

print(dp_print_longest_common_substring(s1, s2, len(s1), len(s2)))



