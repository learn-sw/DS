# i/p : x: abcdgh 
#       y: abedfhr

# output: 4 <abdh>

# problem statement: Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/


def longest_len_lcs(s1, s2,n_size_s1, m_size_s2):

    if n_size_s1==0 or m_size_s2 ==0 :
        return 0
    if s1[n_size_s1-1] == s2[m_size_s2-1]:
        return 1 + longest_len_lcs(s1, s2, n_size_s1-1, m_size_s2-1)
    else:
        return max(longest_len_lcs(s1, s2,  n_size_s1-1, m_size_s2) ,longest_len_lcs(s1, s2,n_size_s1,m_size_s2-1))

s1 = "abcdgh"
s2 = "abedfhr"

# print(longest_len_lcs(s1, s2, len(s1), len(s2)))



# memoization:

r, c = (1001,1001)
m_arr = [[-1 for x in range(r)] for x in range(c)]
def mem_longest_len_lcs(s1, s2,n_size_s1, m_size_s2):
        if n_size_s1==0 or m_size_s2 ==0 :
            return 0
        if m_arr[n_size_s1][m_size_s2]!=-1:
            return m[n_size_s1][m_size_s2]
        if s1[n_size_s1-1] == s2[m_size_s2-1]:
            m_arr[n_size_s1][m_size_s2] =  1 + longest_len_lcs(s1, s2, n_size_s1-1, m_size_s2-1)
            return m_arr[n_size_s1][m_size_s2]
        else:
            m_arr[n_size_s1][m_size_s2] =  max(longest_len_lcs(s1, s2,  n_size_s1-1, m_size_s2) ,longest_len_lcs(s1, s2,n_size_s1,m_size_s2-1))
            return m_arr[n_size_s1][m_size_s2]

s1 = "ab"
s2 = "ef"          
print(mem_longest_len_lcs(s1, s2, len(s1), len(s2)))