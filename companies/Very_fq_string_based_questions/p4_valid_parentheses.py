# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
# Example 4:

# Input: s = "([)]"
# Output: false
# Example 5:

# Input: s = "{[]}"
# Output: true
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# 0 ~ 6 months6 months ~ 1 year1 year ~ 2 years
# amazon 26 bloomberg 15 facebookm 10 microsoft 6 citadel 6 google 5 tesla 4 vmware 4 spotify 4 paypal 3 ebay 3 oracle 3 app;e 2
# adobe 2 yahoo 2 lyft 2 intuit 2 linkedin 7 uber 6 expedia 3 barclays 3 servicenow 3 riot games 3 visa 3 ciscoo 3 sallesforce 3 ....



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        valid_par = { 
            ')':'(',
            '}':'{',
            ']':'['
        }

        temp_list = []
        for char in s:

            if char in valid_par:
                top_ele = temp_list.pop(char)
                if top_ele != valid_par.get(top_ele)
                    return false
            else:
                temp_list.append(char)
        return true
