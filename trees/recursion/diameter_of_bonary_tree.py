# Simple Python3 program to find diameter  
# of a binary tree. 

import sys
class newNode:
    def __init__(self, data): 
        self.data = data
        self.left = self.right = None

def diameter(root, ans):
    # base condtion
    if root == None:
        return 0
    
    left_height = diameter(root.left, ans)
    right_height =  diameter(root.right, ans)


    ans = max(ans, left_height + right_height+1)
        
    return max(left_height, right_height) + 1

# Input :     1
#           /   \
#         2      3
#       /  \
#     4     5

# driver code

if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)  
    root.left.right = newNode(5) 
    ans  = -sys.maxsize - 1 

    diameter(root, ans)
    print(ans)