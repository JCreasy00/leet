# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# recursive solution

def inorderTraversalR(self, root: Optional[TreeNode]) -> List[int]:

    result = [] # a list that contains the traversal
    def inOrder(root): # -> be sure to pass root here 
        # Base Case
        if not root: # if the root does not exist
            return # simply return nothing needs done
        # Recursive Case
        # Begin with left side
        inOrder(root.left)
        # once done and we hit null, append current roots value
        res.append(root.val)
        # after we append a node we alwasy check the right side
        inOrder(root.right)
        
    inOrder(root) # to make sure that the result is updated
    return result


# iterative solution
# this method updates the stack manually

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

    result = []
    stack = [] # the stack we will manipulate on our own
    cur = root # our pointer for the current node

    while cur or stack: # while pointer is not null or stack still contains nodes
        # go left for as long as we can
        while cur:
            stack.append(cur)
            cur = cur.left # continue moving pointer left as far as we can
            # this loop exits when the current pointer is at null
            # this means we can pop from the stack
        cur = stack.pop # pointer now points at the node we just popped
        res.append(cur.val) # append to result since we are all the way left
        cur = cur.right # cur moves down to the right to check that node
        # we just back into the loop again if not null
        # process repeats
    return result
        
       

# to summarize
# inorder traversal starts at the root and moves all the way root.left as far as it can
# last value gets appended, go back a value, append, move right, check all the way left again
