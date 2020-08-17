# Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.
# Examples :

# Input : X = “GeeksforGeeks”, y = “GeeksQuiz”
# Output : 5
# The longest common substring is “Geeks” and is of length 5.

# Input : X = “abcdxyz”, y = “xyzabcd”
# Output : 4
# The longest common substring is “abcd” and is of length 4.

# Input : X = “zxabcdezy”, y = “yzabcdezx”
# Output : 6
# The longest common substring is “abcdez” and is of length 6.

# https://www.geeksforgeeks.org/longest-common-substring-dp-29/

def dp_longest_common_substring(x,y, n, m):
    r,c = n+1, m+1

    dp_arr = [[ -1 for x in range(c)] for x in range(r)]
    result = 0
    for i in range(r):
        for j in range(c):

            if i == 0 or j ==0:
                dp_arr[i][j] = 0
            elif x[i-1] == y[j-1]:
                dp_arr[i][j] = 1 + dp_arr[i-1][j-1]
                result = max(result, dp_arr[i][j]) 
            else:
                dp_arr[i][j] = 0

    print(dp_arr)
    return result




s1 = "abcdxyz"
s2 = "zyabcd"

print(dp_longest_common_substring(s1, s2, len(s1), len(s2)))