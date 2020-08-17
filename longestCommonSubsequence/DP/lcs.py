


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

s1 = "abc"
s2 = "ac"

print(dp_len_longest_common_subsequence(s1, s2, len(s1), len(s2)))