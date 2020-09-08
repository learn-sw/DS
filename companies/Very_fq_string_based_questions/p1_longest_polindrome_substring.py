# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"


# 0 ~ 6 months6 months ~ 1 year1 year ~ 2 years

# Amazon | 34 Facebook | 8 Apple| 8 Google | 7 Microsoft | 6
# Bloomberg | 6 Cisco | 5 eBay | 4 Adobe | 3 Goldman Sachs | 3 Oracle | 2 Morgan Stanley | 2 Nutanix | 2


class Solution(object): 
    def longestPalindrome(self, s):


        def expandCenter(s, left, right):
            while left>=0 and right< len(s) and s[left]==s[right]:
                left -=1
                right +=1
            
            return s[left+1: right]

        if not s: return s
        result = ''
       
        for i in range(len(s)):
            nresult = expandCenter(s, i, i)
            if len(nresult) > len(result):
                result = nresult
            nresult = expandCenter(s, i, i+1)
            if len(nresult) > len(result):
                result = nresult
        return result
            
        
s1 = "efabcddcbahghl"

instance = Solution()
print(instance.longestPalindrome(s1))




