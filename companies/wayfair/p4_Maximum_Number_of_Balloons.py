# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0
 

# Constraints:

# 1 <= text.length <= 10^4
# text consists of lower case English letters only.

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        str_bal = "balloon"
        dict = {}
    
        for x in range(len(text)):
            if text[x] in dict:
                dict[text[x]] +=1
            else:
                 dict[text[x]] =1
        print(dict)
        min_instance = sys.maxsize
        for x in range(len(str_bal)):
            if str_bal[x] not in dict:
                return 0
            elif str_bal[x] in dict:
                
                if(str_bal[x] == "l" or str_bal[x] == "o"):
                    min_instance = min(min_instance, int(dict[str_bal[x]]/2))
                else:
                    min_instance = min(min_instance, dict[str_bal[x]])
        return min_instance
    
        