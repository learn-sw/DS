# // Write code that given the root of two BSTs of integers, finds the greatest common integer in them.


# Given:


#   5
#  / \
# 3   7



#   9
#  / \
# 5   12
#   \
#    7

# Returns:
# 7

from collections import deque 

# this will check if the ele exists in the second tree 
def searchinsecondTree(val,tree):
    node = tree
    
    while node:
        # if value is equal 
        if val == node.val:
            return True
            #greaest_integer = max(greaest_integer,val)
        # if less compare the left tree
        elif val < node.val:
            node = node.left
            
        # if grater compare the right tree
        else:
            node = node.right
        
        # if not foound in the tree return false
        return False
        


def greatest_common_integer(tree1, tree2):
    
    if not tree1 or not tree2:
        return 
    
    
    greaest_integer = None
    # get the root value

    #node = tree1
    queue = deque()
    queue.append(tree1)
    # loop ends after the leaf nodes
    while queue:
        
        # queue to add left and right of the tree 
        node = queue.popleft()
        val = node.val;
        
        if searchinsecondTree(val, tree2):
            greaest_integer = max(greaest_integer,val)
            node = node.right
        
        
        else:
            if node.left:
                queue.append(node.left)
            if  node.right:
                queue.append(node.right)
    return greaest_integer
    
    
    



