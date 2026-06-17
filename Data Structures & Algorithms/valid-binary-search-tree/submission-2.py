# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # time:o(n) space:o(n)
        return self.valid(root, float('-inf'), float('inf'))
    
    def valid(self, node, left_bound, right_bound):
        # null node is valid
        if not node:
            return True
        # if current node is out of the bound
        if not (left_bound < node.val < right_bound):
            return False
        # check left subtree and right subtree
        return self.valid(node.left, left_bound, node.val) and self.valid(node.right, node.val, right_bound)
        
        
        
