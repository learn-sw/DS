# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"


# 0 ~ 6 months6 months ~ 1 year1 year ~ 2 years

# Amazon 31 Facebook 17 Bloomberg 14 Apple 13 Adobe 12 Googl 9 ByteDance 8 
# eBay 5 Goldman Sachs 4 Microsoft 3 Cisco 3 Spotify 3 
# Yahoo 2 Uber 2 VMware 2 Oracle 2 Atlassian 2 Coupang 2 Morgan Stanley 2

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left, max_len = 0 , 0
        map_id = {}

        for right in range(len(s)):

            if s[right] in map_id:

                left = max(left, map_id[s[right]] + 1)

            map_id[s[right]] = right
            max_len = max(max_len,right-left+1 )


        return max_len
            