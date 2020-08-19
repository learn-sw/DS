# Longest Repeating Subsequence

# # Given a string, print the longest repeating subsequence such that the two subsequence don’t have same string character at same position, i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string.
# Example:
# Input: str = "aab"
# Output: "a"
# The two subsequence are 'a'(first) and 'a' 
# (second). Note that 'b' cannot be considered 
# as part of subsequence as it would be at same
# index in both.

# https://www.geeksforgeeks.org/longest-repeated-subsequence/

def dp_len_longest_repeating_subsequence(x, n):
    r,c = n+1,n+1

    dp_arr = [[ -1 for x in range(c)] for x in range(r)]

    for i in range(r):
        for j in range(c):

            if i == 0 or j ==0:
                dp_arr[i][j] = 0
            elif x[i-1] == x[j-1] and i!=j:
                dp_arr[i][j] = 1 + dp_arr[i-1][j-1]
            else:
                dp_arr[i][j] = max(dp_arr[i][j-1], dp_arr[i-1][j])

    print(dp_arr)
    return dp_arr[n][n]

s1 = "aab"
print(dp_len_longest_repeating_subsequence(s1, len(s1)))

s1 = "aabebcdd"
print(dp_len_longest_repeating_subsequence(s1, len(s1)))
