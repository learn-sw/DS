# 242. Valid Anagram
# Easy

# 1754

# 148

# Add to List

# Share
# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict = {}
        for char in s:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
        for char in t:
            if char not in dict:
                return False
            else:
                dict[char] -= 1
            if dict[char] < 0:
                return False
        return True
            
        
        
        #return( ''.join(sorted(s)) == ''.join(sorted(t)))