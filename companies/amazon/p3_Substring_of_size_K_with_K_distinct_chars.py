# Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

# Example 1:

# Input: s = "abcabc", k = 3
# Output: ["abc", "bca", "cab"]
# Example 2:

# Input: s = "abacab", k = 3
# Output: ["bac", "cab"]
# Example 3:

# Input: s = "awaglknagawunagwkwagl", k = 4
# Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
# Explanation: 
# Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl" 
# "wagl" is repeated twice, but is included in the output once.
# Constraints:

# The input string consists of only lowercase English letters [a-z]
# # 0 ≤ k ≤ 26


def kSubstring(s, k):
    if not k or not s:
        return []
    li = []
    len_s = len(s)-k+1
    for i in range(0,len_s):
        if s[i:i+k] not in li and len(set(s[i:i+k])) == k:
            li.append(s[i:i+k])
    return(li)

# def uniquechars(s):
#     li = []:
#     for i in s:
#         if i not in li:
#             li.append(i)
#         else:
#             return False
#     return True



s = "abacab"
k = 3
print(kSubstring(s,k))
s= "awaglknagawunagwkwagl"
k = 4
print(kSubstring(s,k))
s= ""
k = 1
print(kSubstring(s,k))
s= "qe"
k = 0
print(kSubstring(s,k))
#  ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
#  ['wagl', 'aglk', 'glkn', 'lkna', 'knag', 'gawu', 'awun', 'wuna', 'unag', 'nagw', 'agwk', 'kwag']
#  ['wagl', 'aglk', 'glkn', 'lkna', 'knag', 'gawu', 'awun', 'wuna', 'unag', 'nagw', 'agwk', 'kwag', 'agl']