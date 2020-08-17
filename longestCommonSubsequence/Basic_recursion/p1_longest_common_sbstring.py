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

def rec_longest_common_substring(x,y, n, m, count):
    if n_size_s1==0 or m_size_s2 ==0 :
        return 0
    if s1[n_size_s1-1] == s2[m_size_s2-1]:
        count = 1 + longest_len_lcs(s1, s2, n_size_s1-1, m_size_s2-1)
        return count
    else:
        count =  max(longest_len_lcs(s1, s2,  n_size_s1-1, m_size_s2, 0) ,longest_len_lcs(s1, s2,n_size_s1,m_size_s2-1, 0))
        return count

    print(dp_arr)
    return dp_arr[n][m]

s1 = "abc"
s2 = "ac"
count = 0
print(rec_longest_common_substring(s1, s2, len(s1), len(s2), count))