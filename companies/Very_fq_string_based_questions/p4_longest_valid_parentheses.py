# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:

# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# Amazon
# |
# 5

# Apple
# |
# 3

# Uber
# |
# 2

# Citadel
# |
# 2

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        curr_longest = 0 
        
        t_stack = []
        result = 0
        for index in range(len(s)):
            if s[index] == '(':
                t_stack.append(curr_longest)
                curr_longest = 0
            else:
                if t_stack:
                    curr_longest += t_stack.pop() + 2
                    result = max(result,curr_longest )
                else:
                    curr_longest = 0
                
                    
        return result
                